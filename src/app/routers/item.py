from fastapi import APIRouter

item_router = APIRouter()

@item_router.get("/item/{params}")
async def item_by_name(params: str):
    return "Hello world - get item by params" + params
