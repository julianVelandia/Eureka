import json
import os
from typing import List

from internal.information.core.query.get_config import GetConfig as QueryModel
from internal.information.infrastructure.getpath.config.model.path import PathModel

JSON_FILE = '.json'
RELATIVE_PATH = 'Eureka\\internal\\platform\\defaultconfig\\'


class JsonMapping:
    def mapping_json_config_to_path(self, query_model: QueryModel) -> List[PathModel]:
        # TODO try cath finaly
        # TODO def armar url

        with open(self.build_platform_file_path(query_model), 'r') as f:
            data = json.load(f)
            f.close()

        result = []

        for single_path in data:
            single_result = PathModel()
            single_result.__dict__ = single_path
            result.append(single_result)

        return result

    def build_platform_file_path(self, query_model: QueryModel) -> str:
        currently_path = os.getcwd()
        base_path = ''
        for folder in currently_path.split('\\'):
            if folder == 'Eureka':
                break
            base_path += folder + '\\'

        return base_path + RELATIVE_PATH + query_model.get_language() + '\\' + query_model.get_file_name() + JSON_FILE

    def validator_json(self):
        pass
