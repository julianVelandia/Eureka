class Path:
    __section_id: str
    __base_url: str
    __text_tag: str
    __text_class_name: [str]
    __children_tag: str
    __children_class_name: [str]

    def __init__(self,
                 section_id: str,
                 base_url: str,
                 text_tag: str,
                 text_class_name: [str],
                 children_tag: str,
                 children_class_name: [str]):
        self.__section_id = section_id
        self.__base_url = base_url
        self.__text_tag = text_tag
        self.__text_class_name = text_class_name
        self.__children_tag = children_tag
        self.__children_class_name = children_class_name

    def get_section_id(self):
        return self.__section_id

    def get_base_url(self):
        return self.__base_url

    def get_text_tag(self):
        return self.__text_tag

    def get_text_class_name(self):
        return self.__text_class_name

    def get_children_class_name(self):
        return self.__children_class_name

    def get_children_tag(self):
        return self.__children_tag
