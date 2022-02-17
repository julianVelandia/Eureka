from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.query.get_config import GetConfig
from internal.information.core.service.readpath.configfile.ports import ServiceGetPathInterface
from internal.information.infrastructure.getpath.config.mapper.mapper import Mapper
from internal.platform.json.mapping import JsonMapping


class ProcessPathConfig(ServiceGetPathInterface):

    mapper = Mapper()
    json_mapping_interface = JsonMapping()

    def get(self, query: GetConfig) -> PathEntity:
        query_model = self.mapper.query_entity_to_model(query)
        path_model = self.json_mapping_interface.mapping_json_config_to_path(query_model)
        return self.mapper.path_model_to_entity(path_model)
