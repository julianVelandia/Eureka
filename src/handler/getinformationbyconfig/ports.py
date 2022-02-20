from abc import abstractmethod, ABCMeta
from typing import List

from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params


class UseCaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, query: GetConfig) -> List[Information]:
        pass


class MapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def request_to_query(self, request_params: Params) -> GetConfig:
        pass
