from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig
from internal.information.core.usecase.ports import GetConfigServiceInterface
from internal.information.infrastructure.getpath.config.process import ProcessPathConfig


class ServiceGetByConfig(GetConfigServiceInterface):

    path_config = ProcessPathConfig()

    def get_path(self, query: GetConfig) -> [Path]:
        return self.path_config.get(query)
