from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.usecase.get_by_config import RequestService





class Service(RequestService):
    path_config = GetPathService

    def get_information(self, path: Path) -> Information:
        return GetPathService.get(query)
