from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig
from internal.information.core.usecase.get_by_config import GetConfigService


class GetPath:
    def get(self, query: GetConfig) -> Path:
        pass


class Service(GetConfigService):
    path_config = GetPath

    def get_path(self, query: GetConfig) -> Path:
        return GetPath.get(query)
