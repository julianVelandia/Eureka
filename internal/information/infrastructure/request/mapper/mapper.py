from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.core.entity.information import Information as InformationEntity
from internal.information.infrastructure.request.ports import MapperInterface


class Mapper(MapperInterface):

    def information_model_to_entity(self, information_model: InformationModel) -> InformationEntity:
        return InformationEntity(
            information_model.uuid,
            information_model.text,
            information_model.link
        )


