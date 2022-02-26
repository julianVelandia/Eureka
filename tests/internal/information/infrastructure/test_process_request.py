import pytest

from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.infrastructure.request.process import ProcessInformation

process_information = ProcessInformation()


@pytest.mark.parametrize(
    "input_a, expected",
    [(Path(
        section_id='b3cb7919-10c9-4704-bb05-42161060637b',
        base_url='https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia',
        text_tag='div',
        text_class_name=['col-12', 'pb-3'],
        children_tag='h1',
    ), Information(
        uuid='b3cb7919-10c9-4704-bb05-42161060637b',
        link='https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia',
        text='Diplomado en Competencias Digitales para la Docencia',
    ))]
)
def test_get(input_a, expected):
    assert process_information.get(input_a) == expected


@pytest.mark.parametrize(
    "input_a, expected",
    [
        ("https://fastapi.tiangolo.com/", True),
        ("http://fastapi.tiangolo.com/", True),
        ("http://127.0.0.1:8000", True),
        ("http://localhost:8000", True)
    ]
)
def test_validate_url(input_a, expected):
    assert process_information.validate_url(input_a) == expected
