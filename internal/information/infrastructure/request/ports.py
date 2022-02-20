from abc import abstractmethod, ABCMeta

from internal.information.core.entity.information import Information as InformationEntity
from internal.information.infrastructure.request.model.information import InformationModel


class MapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def information_model_to_entity(self, information_model: InformationModel) -> InformationEntity:
        pass
