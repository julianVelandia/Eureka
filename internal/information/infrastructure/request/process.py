from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.entity.information import Information as InformationEntity
from internal.information.core.service.request.ports import RequestServiceInterface
from internal.information.infrastructure.request.mapper.mapper import Mapper
from internal.platform.scraper.request import Request


class ProcessInformation(RequestServiceInterface):
    mapper = Mapper()
    request_interface = Request()

    def get(self, path_entity: PathEntity) -> InformationEntity:
        information_model = self.request_interface.single_request(path_entity)
        return self.mapper.information_model_to_entity(information_model)

    def validate_url(self, url: str) -> bool:
        return self.request_interface.url_is_valid(url)
