from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Path:
    section_id: str
    base_url: str
    __text_tag: str
    text_class_name: [str]
    __children_tag: str


    @property
    def get_text_tag(self):
        return self.__text_tag



    @property
    def get_children_tag(self):
        return self.__children_tag

