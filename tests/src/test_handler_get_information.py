import pytest

from internal.information.core.entity.information import Information
from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.handler import Handler

handler = Handler()


@pytest.mark.parametrize(
    "input_a, expected",
    [(Params("es", "oportunidades"),
      [Information(
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
def test_handler(input_a, expected):
    assert handler.handler(input_a) == expected
