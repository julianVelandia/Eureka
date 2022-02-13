from internal.information.core.query.get_config import GetConfig
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.information.infrastructure.getpath.config.process import MapperInterface
from internal.information.infrastructure.getpath.config.model.path import PathModel as PathPlatformModel
from internal.platform.json.models.query import QueryPlatformModel as QueryPlatformModel
from internal.information.core.entity.path import Path as PathEntity


class Mapper(MapperInterface):
    def query_model_to_platform_model(self, query_model: QueryModel) -> QueryPlatformModel:
        query_platform_model = QueryPlatformModel()
        query_platform_model.language = query_model.language
        query_platform_model.file_name = query_model.file_name
        return query_platform_model

    def path_platform_model_to_entity(self, path_platform_model: PathPlatformModel) -> PathEntity:
        path_entity = PathEntity("", "", [""])
        path_entity.base_url = path_platform_model.base_url
        path_entity.text_tag = path_platform_model.text_tag
        path_entity.text_class_name = path_platform_model.text_class_name

        return path_entity
