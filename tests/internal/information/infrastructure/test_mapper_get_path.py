import pytest

from internal.information.core.entity.path import Path as PathEntity
from internal.information.infrastructure.getpath.config.mapper.mapper import Mapper
from internal.information.infrastructure.getpath.config.model.path import PathModel

mapper = Mapper()

@pytest.mark.parametrize(
    "input_a, expected",
    [
        ([PathModel.new_full_path(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
            "div",
            ["col-12", "pb-3"],
            "h1",
        ),
             PathModel.new_full_path(
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
        assert response[i].section_id == expected[i].section_id
        assert response[i].text_tag == expected[i].text_tag
        assert response[i].base_url == expected[i].base_url
        assert response[i].text_class_name == expected[i].text_class_name
        assert response[i].children_tag == expected[i].children_tag
