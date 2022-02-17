import pytest

from internal.information.infrastructure.getpath.config.model.path import PathModel
from internal.information.infrastructure.getpath.config.model.query import QueryModel
from internal.platform.json.mapping import JsonMapping

json_mapping = JsonMapping()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (QueryModel("es", "oportunidades"), PathModel(
            "https://fastapi.tiangolo.com/",
            "span",
            ["md-ellipsis"]
        ))
        #TODO test cuando falla con el try cath
    ]
)
def test_mapping_json_config_to_path(input_a, expected):
    assert json_mapping.mapping_json_config_to_path(input_a).base_url == expected.base_url
    assert json_mapping.mapping_json_config_to_path(input_a).text_tag == expected.text_tag
    assert json_mapping.mapping_json_config_to_path(input_a).text_class_name == expected.text_class_name


@pytest.mark.parametrize(
    "input_a, expected",
    [
        #TODO en mi pc funciona, pero en otro no
        (QueryModel("es", "oportunidades"), 'C:\\Users\\57315\\Mio\\Eureka\\internal\\platform\\defaultconfig\\es\\oportunidades.json')
    ]
)
def test_build_platform_file_path(input_a, expected):
    assert json_mapping.build_platform_file_path(input_a) == expected
