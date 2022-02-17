from internal.information.core.usecase.get_by_config import UseCaseGetByConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse
from src.handler.getinformationbyconfig.mapper.mapper import Mapper


class Handler:
    mapper = Mapper()
    use_case = UseCaseGetByConfig()

    def handler(self, request_params: Params) -> InformationResponse:

        # TODO Validation params service in platform
        query = self.mapper.request_to_query(request_params)
        # TODO verificar status code
        information = self.use_case.execute(query)

        return self.mapper.entity_to_response(information)


