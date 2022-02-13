from internal.information.core.query.get_config import GetConfig
from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.process import MapperInterface
from internal.information.core.entity.path import Path as PathEntity


class Mapper(MapperInterface):
    def query_entity_to_model(self, query_entity: GetConfig) -> QueryModel:
        query_platform_model = QueryModel()
        query_platform_model.language = query_entity.get_language
        query_platform_model.file_name = query_entity.get_file_name

        return query_platform_model

    def path_model_to_entity(self, path_model: PathModel) -> PathEntity:
        path_entity = PathEntity(
            path_model.base_url,
            path_model.text_tag,
            path_model.text_class_name,
        )

        return path_entity
