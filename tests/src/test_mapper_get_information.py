import pytest

from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.mapper.mapper import Mapper

mapper = Mapper()


@pytest.mark.parametrize(
    "input_a, expected",
    [
        (Params("es", "oportunidades"), GetConfig("es", "oportunidades")),
    ]
)
def test_request_to_query(input_a, expected):
    assert mapper.request_to_query(input_a).get_language() == expected.get_language()
    assert mapper.request_to_query(input_a).get_file_name() == expected.get_file_name()

