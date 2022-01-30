import pytest
from internal.platform.scraper.request import format_class_names


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (["product-name__name", "alkosto-title-color"], "product-name__name alkosto-title-color"),
        (["title", "h1_title", "title_color"], "title h1_title title_color"),
        (["title"], "title"),
    ]
)
def test_format_class_names_when_ok_should_return_true(input_a, expected):
    assert format_class_names(input_a) == expected


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (["product-name__name", " alkosto-title-color"], "product-name__name alkosto-title-color"),
        (["title", "h1_title", " title_color"], "title h1_title title_color"),
        (["title"], " title"),
    ]
)
def test_format_class_names_when_extra_space_should_return_false(input_a, expected):
    assert format_class_names(input_a) != expected