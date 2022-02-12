from internal.information.core.query.get_config import QueryConfig
from internal.information.infrastructure.pathconfig.model.query import QueryModel


class MapperInterface:
    def model_to_domain(self, query_model: QueryModel) -> QueryConfig:
        pass


class ProcessPathConfig:
    mapper: MapperInterface

    def get(self, query_model: QueryModel) -> QueryConfig:
        return MapperInterface.model_to_domain(query_model)
