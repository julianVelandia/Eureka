from abc import ABCMeta, abstractmethod

from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig


class GetConfigService(metaclass=ABCMeta):
    @abstractmethod
    def get_path(self, query: GetConfig) -> Path:
        pass


class GetInformationService:
    @abstractmethod
    def get_information(self, path: Path) -> Information:
        pass

