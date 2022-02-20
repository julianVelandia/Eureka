import pytest

from internal.information.core.query.get_config import GetConfig
from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.platform.json.mapping import JsonMapping

json_mapping = JsonMapping()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (GetConfig("es", "oportunidades"), [
            PathModel(
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
                ["descrp_conv"],
                "p",
            ),
            PathModel(
                "76e8fb84-42b3-4900-a5a8-3a8645385092",
                "https://web.icetex.gov.co/es/-/practical-sustainable-technology",
                "div",
                ["col-12", "pb-3"],
                "h1",
            ),
            PathModel(
                "76e8fb84-42b3-4900-a5a8-3a8645385092",
                "https://web.icetex.gov.co/es/-/practical-sustainable-technology",
                "div",
                ["descrp_conv"],
                "p",),
            PathModel(
                "dfd0f819-3b2e-4b35-b3a0-aa0bbb00d1c2",
                "https://app.becas-santander.com/es/program/"
                "becas-santander-idiomas-online-english-courses-2022-british-council",
                "h1",
                ["text-title", "font-weight-bold"],
                "", ),
            PathModel(
                "dfd0f819-3b2e-4b35-b3a0-aa0bbb00d1c2",
                "https://app.becas-santander.com/es/program/"
                "becas-santander-idiomas-online-english-courses-2022-british-council",
                "p",
                ["pt-4", "ng-star-inserted"],
                "",
            )])
    ]
)
def test_mapping_json_config_to_path(input_a, expected):
    # TODO as list comprehension
    path_model = json_mapping.mapping_json_config_to_path(input_a)
    for i in range(len(path_model)):
        assert path_model[i].section_id == expected[i].section_id
        assert path_model[i].base_url == expected[i].base_url
        assert path_model[i].text_tag == expected[i].text_tag
        assert path_model[i].text_class_name == expected[i].text_class_name
        assert path_model[i].children_tag == expected[i].children_tag


@pytest.mark.parametrize(
    "input_a, expected",
    [
        # TODO en mi pc funciona, pero en otro no
        (GetConfig("es", "oportunidades"),
         'C:\\Users\\57315\\Mio\\Eureka\\internal\\platform\\defaultconfig\\es\\oportunidades.json')
    ]
)
def test_build_platform_file_path(input_a, expected):
    assert json_mapping.build_platform_file_path(input_a) == expected
