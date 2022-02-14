from pydantic import BaseModel


class Params(BaseModel):
    language: str
    config_name: str
