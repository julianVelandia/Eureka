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


class JsonMappingInterface:
    def mapping_json_config_to_path(self, query_model: QueryModel) -> PathModel:
        pass


class ProcessPathConfig(GetPathService):
    mapper = MapperInterface()
    json_mapping_interface = JsonMappingInterface()

    def get(self, query: GetConfig) -> PathEntity:
        query_model = self.mapper.query_entity_to_model(query)
        path_model = self.json_mapping_interface.mapping_json_config_to_path(query_model)
        return self.mapper.path_model_to_entity(path_model)
