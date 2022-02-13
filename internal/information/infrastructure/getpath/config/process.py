from internal.information.core.entity.path import Path as PathEntity
from internal.platform.json.models.query import QueryModel as QueryPlatformModel

from internal.information.infrastructure.getpath.config.model.query import QueryModel


class MapperInterface:
    def model_to_platform_model(self, query_model: QueryModel) -> QueryPlatformModel:
        pass


class jsonMapping:
    def mapping_json_config_to_path(self, query_model: QueryModel) -> PathEntity:
        pass


class ProcessPathConfig:
    mapper: MapperInterface

    def get(self, query_model: QueryModel) -> PathEntity:
        platform_model = MapperInterface.model_to_platform_model(query_model)
        return jsonMapping.mapping_json_config_to_path(platform_model)
