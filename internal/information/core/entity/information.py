class Information:
    __uuid: str
    __link: str
    __text: str

    def __init__(self, uuid: str, link: str, text: str):
        self.__uuid = uuid
        self.__link = link
        self.__text = text

    def get_uuid(self) -> str:
        return self.__uuid

    def get_link(self) -> str:
        return self.__link

    def get_text(self) -> str:
        return self.__text




