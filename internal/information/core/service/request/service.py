from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.usecase.get_by_config import GetInformationService


class RequestService:
    def get(self, path: Path) -> Information:
        pass


class Service(GetInformationService):

    def get_information(self, paths: [Path]) -> [Information]:
        #TODO mirar otras opciones por rendimiento
        #TODO límite de request por response
        #TODO as list comprehension
        information_list = [Information]
        for path in paths:
            information_list.append(RequestService.get(path))

        return information_list