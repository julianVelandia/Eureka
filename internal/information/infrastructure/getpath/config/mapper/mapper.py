from internal.information.core.query.get_config import QueryConfig
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.process import MapperInterface


class Mapper(MapperInterface):
    def model_to_domain(self, query_model: QueryModel) -> QueryConfig:
        query_config = QueryConfig()
        query_config.file_name = query_model.file_name
        return query_config
