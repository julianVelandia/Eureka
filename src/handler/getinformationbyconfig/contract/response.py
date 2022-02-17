# from pydantic import BaseModel


class InformationResponse:
    information: str

    def __init__(self, information: str):
        self.information = information

