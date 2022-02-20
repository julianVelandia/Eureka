from fastapi import APIRouter

from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.handler import Handler as HandlerInformationByConfig

information_router = APIRouter()


@information_router.get("/information/config/{language}/{config_name}")
async def information_by_config(language: str, config_name: str):
    params = Params(language, config_name)

    return HandlerInformationByConfig().handler(params)
