from fastapi import APIRouter

from src.handler.getinformationbyconfig.contract.request import Params

information_router = APIRouter()

@information_router.get("/information/config/{params}")
async def information_by_name(params: Params):
    return handler_item_by_name(params)
