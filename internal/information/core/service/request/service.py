from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.usecase.ports import GetInformationServiceInterface
from internal.information.infrastructure.request.process import ProcessInformation


class ServiceRequest(GetInformationServiceInterface):

    request_service = ProcessInformation()

    def get_information(self, path: Path) -> Information:
        # TODO mirar otras opciones por rendimiento
        # TODO límite de request por response
        # TODO as list comprehension para multiples paths

        # TODO Try cathc
        if self.request_service.validate_url(path.get_base_url()):
            return self.request_service.get(path)
        else:
            return Information("")
