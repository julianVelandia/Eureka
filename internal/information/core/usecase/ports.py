from abc import ABCMeta, abstractmethod
from typing import List

from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig


class GetConfigServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_path(self, query: GetConfig) -> List[Path]:
        pass


class GetInformationServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_information(self, path: List[Path]) -> List[Information]:
        pass
