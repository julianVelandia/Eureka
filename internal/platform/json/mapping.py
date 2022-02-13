import json

from internal.platform.json.models.query import QueryPlatformModel
from internal.information.infrastructure.getpath.config.model.path import PathModel

ABSOLUTE_PATH = '../defaultconfig'
JSON_FILE = '.json'


def mapping_json_config_to_path(query_model: QueryPlatformModel) -> PathModel:
    # TODO try cath finaly
    # TODO def armar url
    f = open(ABSOLUTE_PATH + '/' + query_model.language + '/' + query_model.file_name + JSON_FILE)

    data = json.load(f)

    result = PathModel()
    result.__dict__ = data

    f.close()
    return result
