from internal.information.core.entity.path import Path
from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig


class GetConfigService:
    def get_config(self, query: GetConfig) -> Path:
        pass


class RequestService:
    def get_information(self, path: Path) -> Information:
        pass


class GetByConfig:
    get_config_service: GetConfigService
    requests_service: RequestService

    def execute(self, query: GetConfig) -> Information:
        path = GetConfigService.get_config(query)
        # TODO Manejo de errores

        information = RequestService.get_information(path)

        return information
