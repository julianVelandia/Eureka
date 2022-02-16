from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.entity.information import Information as InformationEntity

from internal.information.core.service.request.service import RequestService
from internal.information.infrastructure.request.ports import MapperInterface, RequestInterface


class ProcessInformation(RequestService):
    mapper = MapperInterface()
    request_interface = RequestInterface()

    def get(self, path_entity: PathEntity) -> InformationEntity:
        path_model = self.mapper.path_entity_to_model(path_entity)
        information_model = self.request_interface.single_request(path_model)
        return self.mapper.information_model_to_entity(information_model)

    def validate_url(self, url: str) -> bool:
        return self.request_interface.url_is_valid(url)
