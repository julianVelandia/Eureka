from abc import ABCMeta, abstractmethod
from typing import List

from internal.information.core.entity.path import Path
from internal.information.infrastructure.getpath.config.model.path import PathModel


class MapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def path_model_to_entity(self, path_model: List[PathModel]) -> List[Path]:
        pass
