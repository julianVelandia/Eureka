from pydantic import BaseModel


class InformationResponse(BaseModel):
    section_id: str
    link: str
    information: str
