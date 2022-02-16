from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse


class UseCase:
    def execute(self, query: GetConfig) -> Information:
        pass


class MapperInterface:
    def request_to_query(self, request_params: Params) -> GetConfig:
        pass

    def entity_to_response(self, information: Information) -> InformationResponse:
        pass


class Handler:
    def handler(self, request_params: Params) -> InformationResponse:
        # TODO Validation params service in platform
        use_case = UseCase()
        mapper = MapperInterface()

        query = mapper.request_to_query(request_params)
        # TODO verificar status coda
        information = use_case.execute(query)

        return mapper.entity_to_response(information)
