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
        ([Information(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
            "information text 1",
        ), Information(
            "b3cb7919-10c9-4704-bb05-42161060637b",
            "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
            "information text 2",
        )],
         [InformationResponse(
             "b3cb7919-10c9-4704-bb05-42161060637b",
             "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
             "information text 1",
         ), InformationResponse(
             "b3cb7919-10c9-4704-bb05-42161060637b",
             "https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia",
             "information text 2",
         )])
    ]
)
def test_entity_to_response(input_a, expected):
    response = mapper.entity_to_response(input_a)
    for i in range(len(response)):
        assert response[i].section_id == expected[i].section_id
        assert response[i].link == expected[i].link
        assert response[i].information == expected[i].information


