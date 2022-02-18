from abc import ABCMeta, abstractmethod

from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.query.get_config import GetConfig
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.model.path import PathModel


class MapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def path_model_to_entity(self, path_model: [PathModel]) -> []:
        pass

    @abstractmethod
    def query_entity_to_model(self, query_entity: GetConfig) -> QueryModel:
        pass

