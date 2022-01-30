import pytest
from internal.platform.scraper.request import format_class_names

NAMES = ["product-name__name", "alkosto-title-color"]
FORMATTED_NAMES = "product-name__name alkosto-title-color"

def test_format_class_names_when_ok_should_return_text():
    assert format_class_names(NAMES) == FORMATTED_NAMES
