import pytest

from internal.information.core.entity.information import Information
from internal.information.infrastructure.request.mapper.mapper import Mapper
from internal.information.infrastructure.request.model.information import InformationModel

mapper = Mapper()


@pytest.mark.parametrize(
    "input_a, expected",
    [(InformationModel(
        "b3cb7919-10c9-4704-bb05-42161060637b",
        "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
        "information text",
    ), Information(
        "b3cb7919-10c9-4704-bb05-42161060637b",
        "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
        "information text", )), ]
)
def test_information_model_to_entity(input_a, expected):
    assert mapper.information_model_to_entity(input_a).text == expected.text
