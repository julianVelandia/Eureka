class Information:
    __uuid: str
    __text: str
    __link: str

    def __init__(self, uuid: str, text: str, link: str):
        self.__text = text
        self.__link = link
        self.__uuid = uuid

    def get_text(self) -> str:
        return self.__text

    def get_link(self) -> str:
        return self.__link

    def get_uuid(self) -> str:
        return self.__uuid
