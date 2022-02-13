class Path:
    __base_url: str
    __text_tag: str
    __text_class_name: [str]

    def __init__(self, base_url: str, text_tag: str, text_class_name: [str]):
        self.__base_url = base_url
        self.__text_tag = text_tag
        self.__text_class_name = text_class_name

    def get_base_url(self):
        return self.__base_url

    def get_text_tag(self):
        return self.__text_tag

    def get_text_class_name(self):
        return self.__text_class_name
