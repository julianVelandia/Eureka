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

    def path_model_to_entity(self, path_model: PathModel) -> PathEntity:
        return PathEntity(
            path_model.base_url,
            path_model.text_tag,
            path_model.text_class_name,
        )
