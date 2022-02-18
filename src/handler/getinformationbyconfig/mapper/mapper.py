from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse
from src.handler.getinformationbyconfig.ports import MapperInterface


class Mapper(MapperInterface):
    def request_to_query(self, request_params: Params) -> GetConfig:
        return GetConfig(
            request_params.language,
            request_params.config_name,
        )

    def entity_to_response(self, information: [Information]) -> []:
        response = []

        for i in information:
            response.append(
                InformationResponse(
                    i.get_uuid(None),
                    i.get_link(None),
                    i.get_text(None),
                ))
        return response
