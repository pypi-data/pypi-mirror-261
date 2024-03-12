import logging

import json
import base64

from mlflow.store.model_registry.abstract_store import AbstractStore
from mlflow.store.entities.paged_list import PagedList
from mlflow.entities.model_registry import RegisteredModel
from mlflow.entities.model_registry import ModelVersion

from mlflow.entities.model_registry.model_version_stages import (
    get_canonical_stage,
    ALL_STAGES,
    DEFAULT_STAGES_FOR_GET_LATEST_VERSIONS,
    STAGE_ARCHIVED,
    STAGE_NONE,
    STAGE_DELETED_INTERNAL,
)

from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import (
    INVALID_PARAMETER_VALUE,
    RESOURCE_ALREADY_EXISTS,
    RESOURCE_DOES_NOT_EXIST,
)

from mlflow.utils.time_utils import get_current_time_millis


from mlflow.utils.search_utils import SearchUtils, SearchModelUtils, SearchModelVersionUtils


from kubernetes import client, config

config.load_kube_config()
co = client.CustomObjectsApi()


class K8sStore(AbstractStore):

    GROUP = "store.mlflow.org"
    VERSION = "v1"
    PLURAL = "registeredmodels"

    K8S_RETRY = 3


    def create_registered_model(self, name, tags=None, description=None):
        logging.info(f"create_registered_model name: {name}, tags: {tags}, description: {description}")
        cur_time = get_current_time_millis()
        body = {
            "apiVersion": "store.mlflow.org/v1",
            "kind": "RegisteredModel",
            "metadata": {
                "name": name
            },
            "spec": {
                "creation_time": cur_time,
                "last_updated_timestamp": cur_time,
                "description": description,
            }
        }
        try:
            created_rm = co.create_namespaced_custom_object(self.GROUP, self.VERSION, 'default', self.PLURAL, body)
            return cr_2_registered_model(created_rm)
        except Exception:
            raise MlflowException(
                f"Registered Model with name={name} create failed",
                RESOURCE_DOES_NOT_EXIST,
            )

    def update_registered_model(self, name, description):
        updated_time = get_current_time_millis()
        body = {
            "spec": {
                "description": description,
                "last_updated_timestamp": updated_time
            }
        }
        try:
            updated_rm = co.patch_namespaced_custom_object(self.GROUP, self.VERSION, 'default', self.PLURAL, name, body)
            return cr_2_registered_model(updated_rm)
        except Exception:
            raise MlflowException(
                f"Registered Model with name={name} update failed",
                RESOURCE_DOES_NOT_EXIST,
            )

    def rename_registered_model(self, name, new_name):
        raise MlflowException(
            f"Rename Registered Model is not supported",
            RESOURCE_DOES_NOT_EXIST,
        )

    def delete_registered_model(self, name):
        try:
            result = co.delete_namespaced_custom_object(self.GROUP, self.VERSION, 'default', self.PLURAL, 'test3')
            if not result["metadata"]["status"] == "Success":
                raise MlflowException(
                    f"Registered Model with name={name} delete failed",
                    RESOURCE_DOES_NOT_EXIST,
                )
        except Exception:
            raise MlflowException(
                f"Registered Model with name={name} update failed",
                RESOURCE_DOES_NOT_EXIST,
            )

    def search_registered_models(self, filter_string=None, max_results=None, order_by=None, page_token=None):
        logging.info(f"search_registered_models filter_string: {filter_string}, max_results: {max_results}, order_by: {order_by}, page_token: {page_token}")

        registered_models = self._list_all_registered_models()
        filtered_rms = SearchModelUtils.filter(registered_models, filter_string)
        sorted_rms = SearchModelUtils.sort(filtered_rms, order_by)
        start_offset = SearchUtils.parse_start_offset_from_page_token(page_token)
        final_offset = start_offset + max_results

        paginated_rms = sorted_rms[start_offset:final_offset]
        next_page_token = None
        if final_offset < len(sorted_rms):
            next_page_token = SearchUtils.create_page_token(final_offset)
        return PagedList(paginated_rms, next_page_token)

    def get_registered_model(self, name):
        logging.info(f"get_registered_model name: {name}")
        return cr_2_registered_model(self._get_rm_by_name(name))


    def get_latest_versions(self, name, stages=None):
        rm = self._get_rm_by_name(name)
        model_versions = self._rm_2_model_versions(name, rm)
        if stages is None or len(stages) == 0:
            expected_stages = {get_canonical_stage(stage) for stage in ALL_STAGES}
        else:
            expected_stages = {get_canonical_stage(stage) for stage in stages}
        latest_versions = {}
        for model_version in model_versions:
            if model_version.current_stage in expected_stages:
                if (
                    model_version.current_stage not in latest_versions
                    or latest_versions[model_version.current_stage].version < model_version.version
                ):
                    latest_versions[model_version.current_stage] = model_version
        return [latest_versions[stage] for stage in expected_stages if stage in latest_versions]

    def set_registered_model_tag(self, name, tag):
        rm = self._get_rm_by_name(name)
        if 'registered_model_tags' not in rm['spec']:
            rm['spec']['registered_model_tags'] = {}
        rm['spec']['registered_model_tags'][tag.key] = tag.value
        self._update_rm(name, rm)

    def delete_registered_model_tag(self, name, key):
        rm = self._get_rm_by_name(name)
        if 'registered_model_tags' in rm['spec'] and key in rm['spec']['registered_model_tags']:
            del rm['spec']['registered_model_tags'][key]
            self._update_rm(name, rm)

    def create_model_version(self, name, source, run_id=None, tags=None, run_link=None, description=None,
                             local_model_path=None):
        for attempt in range(self.K8S_RETRY):
            rm = self._get_rm_by_name(name)
            creation_time = get_current_time_millis()
            version_no = 1
            if 'model_versions' in rm['spec']:
                versions = rm['spec']['model_versions']
                version_no = max(version['version'] for version in versions) + 1
            else:
                rm['spec']['model_versions'] = []
            mv = {
                'version': version_no,
                'creation_time': creation_time,
                'last_updated_timestamp': creation_time,
                'description': description,
                'current_stage': STAGE_NONE,
                'source': source,
                'run_id': run_id,
                'run_link': run_link,
            }
            rm['spec']['model_versions'].append(mv)
            try:
                self._update_rm(name, rm)
                return self._rm_mvs_2_model_version(name, mv)
            except Exception as e:
                logging.error("retry create model version")
                more_retries = self.K8S_RETRY - attempt - 1
                if more_retries == 0:
                    raise MlflowException(
                        f"Model Version creation error (name={name}). Error: {e}. Giving up after "
                        f"{self.K8S_RETRY} attempts."
                    )


    def update_model_version(self, name, version, description):
        rm = self._get_rm_by_name(name)
        if 'model_versions' in rm['spec']:
            mvs = rm['spec']['model_versions']
            model_versions = [mv for mv in mvs if mv['version'] == version]
            if len(model_versions) != 1:
                raise MlflowException(
                    f"Registered Model with name={name} update failed",
                    RESOURCE_DOES_NOT_EXIST,
                )
            else:
                model_versions[0]['description'] = description
            self._update_rm(name, rm)


    def transition_model_version_stage(self, name, version, stage, archive_existing_versions):
        pass

    def delete_model_version(self, name, version):
        rm = self._get_rm_by_name(name)
        if 'model_versions' in rm['spec']:
            mvs = rm['spec']['model_versions']
            model_versions = [mv for mv in mvs if mv['version'] == version]
            if len(model_versions) != 1:
                raise MlflowException(
                    f"Registered Model with name={name} update failed",
                    RESOURCE_DOES_NOT_EXIST,
                )
            else:
                model_versions.remove(model_versions[0])
            self._update_rm(name, rm)

    def get_model_version(self, name, version):
        rm = self._get_rm_by_name(name)
        if 'model_versions' in rm['spec']:
            mvs = rm['spec']['model_versions']
            model_versions = [mv for mv in mvs if mv['version'] == version]
            if len(model_versions) != 1:
                raise MlflowException(
                    f"Registered Model with name={name} update failed",
                    RESOURCE_DOES_NOT_EXIST,
                )
            else:
                return crv_2_model_version(model_versions[0])


    def get_model_version_download_uri(self, name, version):
        pass

    def search_model_versions(self, filter_string=None, max_results=None, order_by=None, page_token=None):
        registered_models = self._list_all_rm()
        model_versions = []
        for rm in registered_models["items"]:
            name = rm["metadata"]["name"]
            model_versions.extend(self._rm_2_model_versions(name, rm))
        filtered_mvs = SearchModelVersionUtils.filter(model_versions, filter_string)

        sorted_mvs = SearchModelVersionUtils.sort(
            filtered_mvs,
            order_by or ["last_updated_timestamp DESC", "name ASC", "version_number DESC"],
        )
        start_offset = SearchUtils.parse_start_offset_from_page_token(page_token)
        final_offset = start_offset + max_results

        paginated_mvs = sorted_mvs[start_offset:final_offset]
        next_page_token = None
        if final_offset < len(sorted_mvs):
            next_page_token = SearchUtils.create_page_token(final_offset)
        return PagedList(paginated_mvs, next_page_token)

    def set_model_version_tag(self, name, version, tag):
        rm = self._get_rm_by_name(name)
        if 'model_versions' in rm['spec']:
            mvs = rm['spec']['model_versions']
            model_versions = [mv for mv in mvs if mv['version'] == version]
            if len(model_versions) != 1:
                raise MlflowException(
                    f"Registered Model with name={name} update failed",
                    RESOURCE_DOES_NOT_EXIST,
                )
            else:
                version_tags = model_versions[0]['model_version_tags']
                version_tags[tag.key] = tag.value
            self._update_rm(name, rm)

    def delete_model_version_tag(self, name, version, key):
        rm = self._get_rm_by_name(name)
        if 'model_versions' in rm['spec']:
            mvs = rm['spec']['model_versions']
            model_versions = [mv for mv in mvs if mv['version'] == version]
            if len(model_versions) != 1:
                raise MlflowException(
                    f"Registered Model with name={name} update failed",
                    RESOURCE_DOES_NOT_EXIST,
                )
            else:
                version_tags = model_versions[0]['model_version_tags']
                if version_tags.__contains__(key):
                    del version_tags[key]
                    self._update_rm(name, rm)
                else:
                    raise MlflowException(
                        f"Registered Model with name={name} update failed",
                        RESOURCE_DOES_NOT_EXIST,
                    )

    def set_registered_model_alias(self, name, alias, version):
        rm = self._get_rm_by_name(name)
        if 'registered_model_aliases' in rm['spec']:
            aliases = rm['registered_model_aliases']
            aliases[alias] = version
            self._update_rm(name, rm)


    def delete_registered_model_alias(self, name, alias):
        rm = self._get_rm_by_name(name)
        if 'registered_model_aliases' in rm['spec']:
            aliases = rm['registered_model_aliases']
            if alias in aliases:
                del aliases[alias]
                self._update_rm(name, rm)

    def get_model_version_by_alias(self, name, alias):
        rm = self._get_rm_by_name(name)
        if 'registered_model_aliases' in rm['spec']:
            aliases = rm['registered_model_aliases']
            if alias in aliases:
                version = aliases[alias]
                mvs = rm['spec']['model_versions']
                model_versions = [mv for mv in mvs if mv['version'] == version]
                return crv_2_model_version(model_versions[0])
        raise MlflowException(
            f"Registered Model with name={name} update failed",
            RESOURCE_DOES_NOT_EXIST,
        )

    def _list_all_registered_models(self):
        k8s_registered_models = co.list_namespaced_custom_object(group=self.GROUP, version=self.VERSION, namespace="default", plural=self.PLURAL)
        registered_models = []
        for item in k8s_registered_models['items']:
            registered_models.append(cr_2_registered_model(item))
        return registered_models


    """
    1. rm means k8s crd registeredmodel
    2. 
    """

    def _list_all_rm(self):


        try:
            k8s_registered_models = co.list_namespaced_custom_object(group=self.GROUP, version=self.VERSION, namespace="default", plural=self.PLURAL)
            return k8s_registered_models
        except Exception:
            raise MlflowException(
                f"List Registered Model failed",
                RESOURCE_DOES_NOT_EXIST,
            )

    def _get_rm_by_name(self, name):
        try:
            rm = co.get_namespaced_custom_object(self.GROUP, self.VERSION, 'default', self.PLURAL, name)
            return rm
        except Exception:
            raise MlflowException(
                f"Registered Model with name={name} not found",
                RESOURCE_DOES_NOT_EXIST,
            )

    def _rm_2_model_versions(self, name, rm):
        model_versions = []
        if not "model_versions" in rm["spec"]:
            return model_versions
        for version in rm["spec"]["model_versions"]:
            model_versions.append(self._rm_mvs_2_model_version(name, version))
        return model_versions


    def _rm_mvs_2_model_version(self, name, model_version):
        mv = ModelVersion(
            name,
            model_version["version"],
            model_version["creation_time"],
            model_version["last_updated_time"],
            model_version["description"],
            # model_version["user_id"],
            current_stage = model_version["current_stage"],
            source = model_version["source"],
            run_id = model_version["run_id"],
            status = model_version["status"],
            # model_version["status_message"],
            run_link = model_version["run_link"],
        )
        return mv

    def _update_rm(self, name, body):
        try:
            co.replace_namespaced_custom_object(self.GROUP, self.VERSION, 'default',  self.PLURAL, name, body)
        except Exception:
            raise MlflowException(
                f"Registered Model with name={name} not found",
                RESOURCE_DOES_NOT_EXIST,
            )


def crv_2_model_version(item):
    return None

def cr_2_registered_model(item):
    print(f'item: {json.dumps(item)}')
    name = item['metadata']['name']
    creation_timestamp = item['spec']['creation_time']
    last_updated_timestamp = item['spec']['last_updated_timestamp']
    description = item['spec']['description']
    rm = RegisteredModel(name=name, creation_timestamp=creation_timestamp, last_updated_timestamp=last_updated_timestamp, description=description)
    return rm