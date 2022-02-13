import json

from internal.platform.json.models.jsonString import JsonString
from internal.platform.json.models.query import QueryModel
from internal.information.core.entity.path import Path as PathEntity


def mapping_json_config_to_path(query_model: QueryModel) -> PathEntity:
    json_string = get_json_string(query_model)

    data = json.loads(json_string.default_string)
    result = PathEntity("", "", [""])
    result.__dict__ = data
    return result


def get_json_string(query_model: QueryModel) -> JsonString:
    open_json_file(query_model)
    pass


def open_json_file(query_model: QueryModel):
    pass
