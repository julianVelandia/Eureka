from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.entity.information import Information as InformationEntity

from internal.information.core.service.request.service import RequestService
from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.infrastructure.request.model.path import PathModel


class MapperInterface:
    def information_model_to_entity(self, information_model: InformationModel) -> InformationEntity:
        pass

    def path_entity_to_model(self, path_entity: PathEntity) -> PathModel:
        pass


class RequestInterface:
    def single_request(self, path_model: PathModel) -> InformationModel:
        pass

    def url_is_valid(self, path: str) -> bool:
        pass


class ProcessInformation(RequestService):
    mapper: MapperInterface

    def get(self, path_entity: PathEntity) -> InformationEntity:
        path_model = MapperInterface.path_entity_to_model(path_entity)
        information_model = RequestInterface.single_request(path_model)
        return MapperInterface.information_model_to_entity(information_model)

    def validate_url(self, url: str) -> bool:
        return RequestInterface.url_is_valid(url)
