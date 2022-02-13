from internal.information.core.entity.path import Path
from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import QueryConfig


class GetConfigService:
    def get_config(self, query: QueryConfig) -> Path:
        pass


class RequestService:
    def get_config(self, path: Path) -> Information:
        pass


class GetByConfig:
    get_config_service: GetConfigService
    requests_service: RequestService

    def execute(self, query: QueryConfig) -> Information:
        path = GetConfigService.get_config(query)
        #TODO Manejo de errores

        information = RequestService.get_config(path)

        return information