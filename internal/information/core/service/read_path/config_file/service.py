from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig
from internal.information.core.service.read_path.config_file.ports import GetPathService
from internal.information.core.usecase.get_by_config import GetConfigService


class Service(GetConfigService):
    path_config = GetPathService()

    def get_path(self, query: GetConfig) -> Path:
        return self.path_config.get(query)
