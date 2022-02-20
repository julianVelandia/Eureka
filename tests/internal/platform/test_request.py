import pytest

from internal.information.core.entity.path import Path
from internal.information.infrastructure.request.model.information import InformationModel
from internal.platform.scraper.request import Request

request = Request()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (Path(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
            "div",
            ["col-12", "pb-3"],
            "h1",
        ), InformationModel(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "Diplomado en Competencias Digitales para la Docencia",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
        )),

        (Path(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://fastapi.tiangolo.com/",
            "span",
            ["md-ellipsis"],
            "",
        ), InformationModel(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "\n            FastAPI\n          ",
            "https://fastapi.tiangolo.com/",
        ))
    ]
)
def test_single_request(input_a, expected):
    assert request.single_request(input_a).text == expected.text
    assert request.single_request(input_a).link == expected.link
    assert request.single_request(input_a).uuid == expected.uuid


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (["product-name__name", "title-color"], "product-name__name title-color"),
        (["title", "h1_title", "title_color"], "title h1_title title_color"),
        (["title"], "title"),
    ]
)
def test_format_class_names(input_a, expected):
    assert request.format_class_names(input_a) == expected


@pytest.mark.parametrize(
    "input_a, expected",
    [
        ("https://fastapi.tiangolo.com/", True),
        ("http://fastapi.tiangolo.com/", True),
        ("http://127.0.0.1:8000", True),
        ("http://localhost:8000", True)
    ]
)
def test_url_is_valid(input_a, expected):
    assert request.url_is_valid(input_a) == expected
