from pydantic import BaseModel


class InformationResponse(BaseModel):
    information: str
