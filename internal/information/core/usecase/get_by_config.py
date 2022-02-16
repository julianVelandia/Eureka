from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from internal.information.core.usecase.ports import GetConfigService, GetInformationService
from src.handler.getinformationbyconfig.ports import UseCaseInterface


class GetByConfig(UseCaseInterface):
    get_config_service = GetConfigService()
    get_information_service = GetInformationService()

    def execute(self, query: GetConfig) -> Information:
        path = self.get_config_service.get_path(query)
        # TODO Manejo de errores

        full_information = self.get_information_service.get_information(path)

        return full_information
