from internal.information.core.query.get_config import QueryConfig
from internal.information.infrastructure.pathconfig.model.query import QueryModel


class Mapper:
    def model_to_domain(self, query_model: QueryModel) -> QueryConfig:
        pass


class ProcessPathConfig:
    mapper: Mapper

    def get(self, query_model: QueryModel) -> QueryConfig:
        return Mapper.model_to_domain(query_model)
