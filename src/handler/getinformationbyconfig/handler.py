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
    def handler(self, requestParams: Params) -> InformationResponse:
        #TODO Validation params service in platform

        query = MapperInterface.request_to_query(requestParams)
        #TODO verificar status coda
        information = UseCase.execute(query)

        return MapperInterface.entity_to_response(information)