# from pydantic import BaseModel


class InformationResponse:
    section_id: str
    link: str
    information: str

    def __init__(self, section_id: str, link: str, information: str):
        self.section_id = section_id
        self.link = link
        self.information = information
