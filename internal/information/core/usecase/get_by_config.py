from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from internal.information.core.service.readpath.configfile.service import ServiceGetByConfig
from internal.information.core.service.request.service import ServiceRequest
from src.handler.getinformationbyconfig.ports import UseCaseInterface


class UseCaseGetByConfig(UseCaseInterface):

    get_config_service = ServiceGetByConfig()
    get_information_service = ServiceRequest()

    def execute(self, query: GetConfig) -> Information:
        path = self.get_config_service.get_path(query)
        # TODO Manejo de errores

        full_information = self.get_information_service.get_information(path)

        return full_information

