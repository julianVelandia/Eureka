import pytest

from internal.information.core.entity.information import Information
from internal.information.core.query.get_config import GetConfig
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.contract.response import InformationResponse
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



@pytest.mark.parametrize(
    "input_a, expected",
    [
        (Information("information text"), InformationResponse("information text")),
    ]
)
def test_entity_to_response(input_a, expected):
    assert mapper.entity_to_response(input_a).information == expected.information

