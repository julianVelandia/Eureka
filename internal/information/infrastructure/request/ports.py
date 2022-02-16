from abc import abstractmethod, ABCMeta

from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.entity.information import Information as InformationEntity
from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.infrastructure.request.model.path import PathModel


class MapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def information_model_to_entity(self, information_model: InformationModel) -> InformationEntity:
        pass

    @abstractmethod
    def path_entity_to_model(self, path_entity: PathEntity) -> PathModel:
        pass


