import json

from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.infrastructure.getpath.config.process import ProcessPathConfig

ABSOLUTE_PATH = '../defaultconfig'
JSON_FILE = '.json'


class JsonMapping(ProcessPathConfig):
    def mapping_json_config_to_path(self, query_model: QueryModel) -> PathModel:
        # TODO try cath finaly
        # TODO def armar url
        f = open(ABSOLUTE_PATH + '/' + query_model.language + '/' + query_model.file_name + JSON_FILE)

        data = json.load(f)

        result = PathModel()
        result.__dict__ = data

        f.close()
        return result
