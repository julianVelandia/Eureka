from dataclasses import dataclass


@dataclass(frozen=True)
class Information:
    uuid: str
    link: str
    text: str
