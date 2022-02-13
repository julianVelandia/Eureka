from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig


class GetPath:
    def get(self, query: GetConfig) -> Path:
        pass


class Service:
    path_config = GetPath

    def get_config(self, query: GetConfig) -> Path:
        return GetPath.get(query)
