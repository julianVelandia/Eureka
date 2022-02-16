from abc import abstractmethod, ABCMeta

from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig


class GetPathService(metaclass=ABCMeta):
    @abstractmethod
    def get(self, query: GetConfig) -> Path:
        pass
