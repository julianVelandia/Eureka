from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.query.get_config import GetConfig
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.platform.json.models.query import QueryPlatformModel as QueryPlatformModel
from internal.information.infrastructure.getpath.config.model.path import PathModel as PathPlatformModel



class MapperInterface:
    def path_platform_model_to_entity(self, path_platform_model: PathPlatformModel) -> PathEntity:
        pass

    def query_model_to_platform_model(self, query_model: QueryModel) -> QueryPlatformModel:
        pass


class jsonMappingInterface:
    def mapping_json_config_to_path(self, query_model: QueryModel) -> PathEntity:
        pass


class ProcessPathConfig:
    mapper: MapperInterface

    def get(self, query_model: QueryModel) -> PathEntity:
        platform_model = MapperInterface.query_model_to_platform_model(query_model)
        path_platform_model = jsonMappingInterface.mapping_json_config_to_path(platform_model)
        return MapperInterface.path_platform_model_to_entity(path_platform_model)