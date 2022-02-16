import json
import os

from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.infrastructure.getpath.config.process import ProcessPathConfig

JSON_FILE = '.json'
RELATIVE_PATH = 'Eureka\\internal\\platform\\defaultconfig\\'


class JsonMapping(ProcessPathConfig):
    def mapping_json_config_to_path(self, query_model: QueryModel) -> PathModel:
        # TODO try cath finaly
        # TODO def armar url

        with open(self.build_platform_file_path(query_model), 'r') as f:
            data = json.load(f)

            result = PathModel("", "", [""])
            result.__dict__ = data

            f.close()
        return result

    def build_platform_file_path(self, query_model: QueryModel) -> str:
        currently_path = os.getcwd()
        base_path = ''
        for folder in currently_path.split('\\'):
            if folder == 'Eureka':
                break
            base_path += folder + '\\'


        return base_path + RELATIVE_PATH + query_model.language + '\\' + query_model.file_name + JSON_FILE


if __name__ == "__main__":
    j = JsonMapping()
    print(j.mapping_json_config_to_path(QueryModel("es", "oportunidades")).text_class_name)
