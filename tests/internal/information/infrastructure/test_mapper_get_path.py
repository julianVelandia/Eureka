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
        ([PathModel(
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
             ),
         ], [
             PathEntity(
                 "b3cb7919-10c9-4704-bb05-42161060637b",
                 "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
                 "div",
                 ["col-12", "pb-3"],
                 "h1",
             ),
             PathEntity(
                 "b3cb7919-10c9-4704-bb05-42161060637b",
                 "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
                 "div",
                 ["col-12", "pb-3"],
                 "h1",
             ),
         ])
    ]
)
def test_path_model_to_entity(input_a, expected):
    response = mapper.path_model_to_entity(input_a)
    for i in range(len(response)):
        assert response[i].get_section_id() == expected[i].get_section_id()
        assert response[i].get_text_tag() == expected[i].get_text_tag()
        assert response[i].get_base_url() == expected[i].get_base_url()
        assert response[i].get_text_class_name() == expected[i].get_text_class_name()
        assert response[i].get_children_tag() == expected[i].get_children_tag()
