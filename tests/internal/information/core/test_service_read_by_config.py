import pytest

from internal.information.core.entity.path import Path
from internal.information.core.query.get_config import GetConfig
from internal.information.core.service.readpath.configfile.service import ServiceGetByConfig

service_get_by_config = ServiceGetByConfig()


@pytest.mark.parametrize(
    "input_a, expected",
    [(GetConfig("es", "oportunidades"),
      [Path(
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
          children_tag="",
      ), ])]
)
def test_get(input_a, expected):
    assert service_get_by_config.get_path(input_a) == expected
