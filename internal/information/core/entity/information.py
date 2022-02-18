from dataclasses import dataclass


@dataclass(frozen=True)
class Information:
    __uuid: str
    __link: str
    __text: str

    @property
    def get_uuid(self) -> str:
        return self.__uuid

    @property
    def get_link(self) -> str:
        return self.__link

    @property
    def get_text(self) -> str:
        return self.__text




