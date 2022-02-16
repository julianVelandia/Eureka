from fastapi import APIRouter

from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.handler import Handler as handler_information_by_config


information_router = APIRouter()

#make funtion get url
@information_router.get("/information/config/{language}/{config_name}")
async def information_by_config(language: str, config_name: str):
    params = Params()
    params.language = language
    params.config_name = config_name
    return handler_information_by_config().handler(params)
