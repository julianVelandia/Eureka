import pytest

from internal.information.infrastructure.request.model.information import InformationModel
from internal.information.infrastructure.request.model.path import PathModel
from internal.platform.scraper.request import Request

request = Request()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (PathModel("https://fastapi.tiangolo.com/", "span", ["md-ellipsis"]), InformationModel("\n            FastAPI\n          "))
    ]
)
def test_single_request(input_a, expected):
    assert request.single_request(input_a).text == expected.text


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


