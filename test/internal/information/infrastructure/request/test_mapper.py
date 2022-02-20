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
        (InformationModel("information text"), Information("information text")),
    ]
)
def test_information_model_to_entity(input_a, expected):
    assert mapper.information_model_to_entity(input_a).get_text() == expected.get_text()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (PathEntity(
            "https://fastapi.tiangolo.com/",
            "span",
            ["md-ellipsis"]
        ),
         PathModel(
             "https://fastapi.tiangolo.com/",
             "span",
             ["md-ellipsis"]
         ))
    ]
)
def test_path_entity_to_model(input_a, expected):
    assert mapper.path_entity_to_model(input_a).text_tag == expected.text_tag
    assert mapper.path_entity_to_model(input_a).base_url == expected.base_url
    assert mapper.path_entity_to_model(input_a).text_class_name == expected.text_class_name
