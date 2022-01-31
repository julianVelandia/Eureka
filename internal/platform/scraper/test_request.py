import pytest
from internal.platform.scraper.request import format_class_names, single_request, url_is_valid
from internal.platform.scraper.models.path import Path
from internal.platform.scraper.models.information import Information


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (Path("https://fastapi.tiangolo.com/", "span", ["md-ellipsis"]), Information("\n            FastAPI\n          "))
    ]
)
def test_single_request_when_ok_should_return_text(input_a, expected):
    assert single_request(input_a).text == expected.text


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (["product-name__name", "title-color"], "product-name__name title-color"),
        (["title", "h1_title", "title_color"], "title h1_title title_color"),
        (["title"], "title"),
    ]
)
def test_format_class_names_when_ok_should_return_true(input_a, expected):
    assert format_class_names(input_a) == expected


@pytest.mark.parametrize(
    "input_a, expected",
    [
        ("https://fastapi.tiangolo.com/", True),
        ("http://fastapi.tiangolo.com/", True),
        ("http://127.0.0.1:8000", True),
        ("http://localhost:8000", True)
    ]
)
def test_url_is_valid_when_ok_should_return_text(input_a, expected):
    assert url_is_valid(input_a) == expected


