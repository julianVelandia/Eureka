from abc import ABCMeta, abstractmethod

from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path


class RequestService(metaclass=ABCMeta):
    @abstractmethod
    def get(self, path: Path) -> Information:
        pass

    @abstractmethod
    def validate_url(self, url: str) -> bool:
        pass
