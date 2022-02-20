from internal.information.core.entity.information import Information
from internal.information.core.usecase.get_by_config import UseCaseGetByConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.mapper.mapper import Mapper


class Handler:
    mapper = Mapper()
    use_case = UseCaseGetByConfig()

    def handler(self, request_params: Params) -> list[Information]:

        query = self.mapper.request_to_query(request_params)
        return self.use_case.execute(query)
