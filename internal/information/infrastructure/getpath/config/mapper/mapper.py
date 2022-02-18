from typing import List

from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.core.entity.path import Path as PathEntity, Path
from internal.information.infrastructure.getpath.config.ports import MapperInterface


class Mapper(MapperInterface):
    def path_model_to_entity(self, path_model: List[PathModel]) -> List[Path]:
        path_entity = []

        for p in path_model:
            path_entity.append(
                PathEntity(
                    p.section_id,
                    p.base_url,
                    p.text_tag,
                    p.text_class_name,
                    p.children_tag,
                ))

        return path_entity

