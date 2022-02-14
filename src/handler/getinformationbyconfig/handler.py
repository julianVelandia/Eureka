from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse


class UseCase:
    def execute(self, query: GetConfig) -> Information:
        pass


class MapperInterface:
    def request_to_query(self, request: Params) -> GetConfig:
        pass

    def entity_to_response(self, information: Information) -> InformationResponse:
        pass

class Handler:
