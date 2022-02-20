from typing import List

from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig
from internal.information.core.service.readpath.configfile.ports import ServiceGetPathInterface
from internal.information.infrastructure.getpath.config.mapper.mapper import Mapper
from internal.platform.json.mapping import JsonMapping


class ProcessPathConfig(ServiceGetPathInterface):

    mapper = Mapper()
    json_mapping_interface = JsonMapping()

    def get(self, query: GetConfig) -> List[Path]:
        path_model = self.json_mapping_interface.mapping_json_config_to_path(query)
        return self.mapper.path_model_to_entity(path_model)
