from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.query.get_config import GetConfig
from internal.information.core.service.read_path.config_file.service import GetPathService
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.model.path import PathModel


class MapperInterface:
    def path_model_to_entity(self, path_model: PathModel) -> PathEntity:
        pass

    def query_entity_to_model(self, query_entity: GetConfig) -> QueryModel:
        pass


class jsonMappingInterface:
    def mapping_json_config_to_path(self, query_model: QueryModel) -> PathModel:
        pass


class ProcessPathConfig(GetPathService):
    mapper: MapperInterface

    def get(self, query: GetConfig) -> PathEntity:
        query_model = MapperInterface.query_entity_to_model(query)
        path_model = jsonMappingInterface.mapping_json_config_to_path(query_model)
        return MapperInterface.path_model_to_entity(path_model)
