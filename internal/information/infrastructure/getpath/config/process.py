from internal.information.core.query.get_config import QueryConfig as QueryEntity
from internal.information.infrastructure.getpath.config.model.query import QueryModel


class MapperInterface:
    def model_to_domain(self, query_model: QueryModel) -> QueryEntity:
        pass

    def json_to_model(self, query_model: QueryModel, json_config) -> QueryEntity:
        pass




class ProcessPathConfig:
    mapper: MapperInterface

    def get(self, query_model: QueryModel) -> QueryEntity:
        return MapperInterface.model_to_domain(query_model)
