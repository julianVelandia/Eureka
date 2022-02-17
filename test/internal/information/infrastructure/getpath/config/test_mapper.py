import pytest

from internal.information.core.entity.path import Path as PathEntity
from internal.information.core.query.get_config import GetConfig
from internal.information.infrastructure.getpath.config.mapper.mapper import Mapper
from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.infrastructure.getpath.config.model.query import QueryModel

mapper = Mapper()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (GetConfig("es", "oportunidades"), QueryModel("es", "oportunidades")),
    ]
)
def test_query_entity_to_model(input_a, expected):
    assert mapper.query_entity_to_model(input_a).language == expected.language
    assert mapper.query_entity_to_model(input_a).file_name == expected.file_name


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (PathModel(
            "https://fastapi.tiangolo.com/",
            "span",
            ["md-ellipsis"]
        ),
         PathEntity(
             "https://fastapi.tiangolo.com/",
             "span",
             ["md-ellipsis"]
         ))
    ]
)
def test_path_model_to_entity(input_a, expected):
    assert mapper.path_model_to_entity(input_a).get_text_tag() == expected.get_text_tag()
    assert mapper.path_model_to_entity(input_a).get_base_url() == expected.get_base_url()
    assert mapper.path_model_to_entity(input_a).get_text_class_name() == expected.get_text_class_name()
