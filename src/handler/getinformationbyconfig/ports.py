from abc import abstractmethod, ABCMeta

from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse


class UseCaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, query: GetConfig) -> [Information]:
        pass


class MapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def request_to_query(self, request_params: Params) -> GetConfig:
        pass

    @abstractmethod
    def entity_to_response(self, information: [Information]) -> []:
        pass
