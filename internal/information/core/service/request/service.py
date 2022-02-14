from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.usecase.get_by_config import GetInformationService


class RequestService:
    def get(self, path: Path) -> Information:
        pass

    def validate_url(self, url: str) -> bool:
        pass

class Service(GetInformationService):

    def get_information(self, path: Path) -> Information:
        #TODO mirar otras opciones por rendimiento
        #TODO límite de request por response
        #TODO as list comprehension para multiples paths

        #TODO Try cathc
        if RequestService.validate_url(path.get_base_url()):
            return RequestService.get(path)
        else:
            return Information("")

