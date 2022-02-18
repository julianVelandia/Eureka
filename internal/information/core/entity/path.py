from dataclasses import dataclass


@dataclass(frozen=True)
class Path:
    __section_id: str
    __base_url: str
    __text_tag: str
    __text_class_name: [str]
    __children_tag: str

    @property
    def get_section_id(self):
        return self.__section_id

    @property
    def get_base_url(self):
        return self.__base_url

    @property
    def get_text_tag(self):
        return self.__text_tag

    @property
    def get_text_class_name(self):
        return self.__text_class_name

    @property
    def get_children_tag(self):
        return self.__children_tag
