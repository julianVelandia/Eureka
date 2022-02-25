import pytest

from internal.information.core.entity.information import Information
from internal.information.core.entity.path import Path
from internal.information.core.service.request.service import ServiceRequest

service_request = ServiceRequest()


@pytest.mark.parametrize(
    "input_a, expected",
    [([Path(
        section_id='b3cb7919-10c9-4704-bb05-42161060637b',
        base_url='https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia',
        text_tag='div',
        text_class_name=['col-12', 'pb-3'],
        children_tag='h1',
    ), Path(
        section_id='b3cb7919-10c9-4704-bb05-42161060637b',
        base_url='https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia',
        text_tag='div',
        text_class_name=['descrp_conv'],
        children_tag='p',
    ), Path(
        section_id='76e8fb84-42b3-4900-a5a8-3a8645385092',
        base_url='https://web.icetex.gov.co/es/-/practical-sustainable-technology',
        text_tag='div',
        text_class_name=['col-12', 'pb-3'],
        children_tag='h1',
    ), Path(
        section_id='76e8fb84-42b3-4900-a5a8-3a8645385092',
        base_url='https://web.icetex.gov.co/es/-/practical-sustainable-technology',
        text_tag='div',
        text_class_name=['descrp_conv'],
        children_tag='p',
    ), Path(
        section_id="dfd0f819-3b2e-4b35-b3a0-aa0bbb00d1c2",
        base_url="https://fastapi.tiangolo.com/",
        text_tag="span",
        text_class_name=["md-ellipsis"],
        children_tag=""),
    ], [Information(
        uuid='b3cb7919-10c9-4704-bb05-42161060637b',
        link='https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia',
        text='Diplomado en Competencias Digitales para la Docencia',
    ), Information(
        uuid='b3cb7919-10c9-4704-bb05-42161060637b',
        link='https://web.icetex.gov.co/es/-/diplomado-competencias-digitales-docencia',
        text='El programa ofrece competencias al docente para diseñar, implementar y evaluar experiencias de aprendizaje mediadas por las tecnologías que hagan más efectivo el proceso de aprendizaje de los estudiantes.',
    ), Information(
        uuid='76e8fb84-42b3-4900-a5a8-3a8645385092',
        link='https://web.icetex.gov.co/es/-/practical-sustainable-technology',
        text='Practical Sustainable Technology as a Tool to Tackle the Climate Change',
    ), Information(
        uuid='76e8fb84-42b3-4900-a5a8-3a8645385092',
        link='https://web.icetex.gov.co/es/-/practical-sustainable-technology',
        text='El curso tiene como objetivo mejorar el conocimiento sobre el uso de técnicas y tecnologías sostenibles a través del enfoque de la ingeniería ambiental.',
    ), Information(
        uuid='dfd0f819-3b2e-4b35-b3a0-aa0bbb00d1c2',
        link='https://fastapi.tiangolo.com/',
        text='\n            FastAPI\n          ',
    )])]
)
def test_get(input_a, expected):
    assert service_request.get_information(input_a) == expected
