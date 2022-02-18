from internal.information.core.query.get_config import GetConfig
from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.core.entity.path import Path as PathEntity
from internal.information.infrastructure.getpath.config.ports import MapperInterface


class Mapper(MapperInterface):
    def query_entity_to_model(self, query_entity: GetConfig) -> QueryModel:
        query_platform_model = QueryModel(
            query_entity.get_language(),
            query_entity.get_file_name(),
        )

        return query_platform_model

    def path_model_to_entity(self, path_model: [PathModel]) -> []:
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
