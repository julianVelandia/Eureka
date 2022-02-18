from abc import abstractmethod, ABCMeta
from typing import List

from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig


class ServiceGetPathInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self, query: GetConfig) -> List[Path]:
        pass
