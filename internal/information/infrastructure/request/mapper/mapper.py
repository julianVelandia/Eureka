from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.infrastructure.request.model.path import PathModel
from internal.information.infrastructure.request.process import MapperInterface
from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.entity.information import Information as InformationEntity


class Mapper(MapperInterface):

    def information_model_to_entity(self, information_model: InformationModel) -> InformationEntity:
        return InformationEntity(information_model.text)

    def path_entity_to_model(self, path_entity: PathEntity) -> PathModel:
        path_model = PathModel(
            path_entity.get_base_url(),
            path_entity.get_text_tag(),
            path_entity.get_text_class_name()
        )

        return path_model
