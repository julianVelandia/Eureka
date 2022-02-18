from typing import List

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from internal.information.core.entity.information import Information
from internal.information.core.usecase.get_by_config import UseCaseGetByConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse
from src.handler.getinformationbyconfig.mapper.mapper import Mapper


class Handler:
    mapper = Mapper()
    use_case = UseCaseGetByConfig()

    def handler(self, request_params: Params) -> list[Information]:

        # TODO Validation params service in platform
        query = self.mapper.request_to_query(request_params)
        # TODO verificar status code
        return self.use_case.execute(query)



