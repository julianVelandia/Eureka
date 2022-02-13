import json

from internal.information.core.service.read_path.config_file.service import GetPathService
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.model.path import PathModel

ABSOLUTE_PATH = '../defaultconfig'
JSON_FILE = '.json'


class ProcessPathConfig(GetPathService):
    def mapping_json_config_to_path(self, query_model: QueryModel) -> PathModel:
        # TODO try cath finaly
        # TODO def armar url
        f = open(ABSOLUTE_PATH + '/' + query_model.language + '/' + query_model.file_name + JSON_FILE)

        data = json.load(f)

        result = PathModel()
        result.__dict__ = data

        f.close()
        return result
