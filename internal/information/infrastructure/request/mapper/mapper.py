from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.infrastructure.request.model.path import PathModel
from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.entity.information import Information as InformationEntity
from internal.information.infrastructure.request.ports import MapperInterface


class Mapper(MapperInterface):

    def information_model_to_entity(self, information_model: InformationModel) -> InformationEntity:
        return InformationEntity(
            information_model.uuid,
            information_model.text,
            information_model.link
        )

    def path_entity_to_model(self, path_entity: PathEntity) -> PathModel:
        path_model = PathModel(
            path_entity.get_section_id(),
            path_entity.get_base_url(),
            path_entity.get_text_tag(),
            path_entity.get_text_class_name(),
            path_entity.get_children_tag(),
        )

        return path_model
