class GetConfig:
    __language: str
    __file_name: str

    def __init__(self, language: str, file_name: str):
        self.__language = language
        self.__file_name = file_name

    def get_language(self) -> str:
        return self.__language

    def get_file_name(self) -> str:
        return self.__file_name
