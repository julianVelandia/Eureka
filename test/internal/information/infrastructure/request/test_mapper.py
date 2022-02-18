import pytest

from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path as PathEntity
from internal.information.infrastructure.request.mapper.mapper import Mapper
from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.infrastructure.request.model.path import PathModel

mapper = Mapper()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (InformationModel(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
            "information text",
        ),
         Information(
             "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
             "information text",
         )),
    ]
)
def test_information_model_to_entity(input_a, expected):
    assert mapper.information_model_to_entity(input_a).get_text() == expected.get_text()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (PathEntity(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
            "div",
            ["col-12", "pb-3"],
            "h1",
        ),
         PathModel(
             "b3cb7919-10c9-4704-bb05-42161060637b",
             "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
             "div",
             ["col-12", "pb-3"],
             "h1",
         ))
    ]
)
def test_path_entity_to_model(input_a, expected):
    assert mapper.path_entity_to_model(input_a).section_id == expected.section_id
    assert mapper.path_entity_to_model(input_a).text_tag == expected.text_tag
    assert mapper.path_entity_to_model(input_a).base_url == expected.base_url
    assert mapper.path_entity_to_model(input_a).text_class_name == expected.text_class_name
    assert mapper.path_entity_to_model(input_a).children_tag == expected.children_tag
