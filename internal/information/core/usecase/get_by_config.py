from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig


class GetConfigService:
    def get_path(self, query: GetConfig) -> Path:
        pass


class GetInformationService:
    def get_information(self, path: Path) -> Information:
        pass


class GetByConfig:
    get_config_service: GetConfigService
    get_information_service: GetInformationService

    def execute(self, query: GetConfig) -> Information:
        path = GetConfigService.get_path(query)
        # TODO Manejo de errores

        full_information = GetInformationService.get_information(path)

        return full_information
