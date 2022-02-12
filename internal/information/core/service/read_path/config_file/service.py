from internal.information.core.query.get_config import QueryConfig
from internal.information.core.entity.path import Path
from internal.information.infrastructure.getpath.config.model.query import QueryModel


class PathConfig:
    def get(self, query_model: QueryModel) -> QueryConfig:
        pass

class MapperInterface:
    def
        pass

class Service:
    path_config = PathConfig
    mapper = MapperInterface

    def get_config(self, query: QueryConfig) -> Path:
