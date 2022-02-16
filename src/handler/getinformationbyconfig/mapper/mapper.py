from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse
from src.handler.getinformationbyconfig.handler import MapperInterface


class Mapper(MapperInterface):
    def request_to_query(self, request_params: Params) -> GetConfig:
        return GetConfig(
            request_params.language,
            request_params.config_name,
        )

    def entity_to_response(self, information: Information) -> InformationResponse:
        information_response = InformationResponse()
        information_response.information = information.get_text()
        return information_response
