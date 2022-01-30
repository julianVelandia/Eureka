from fastapi import APIRouter

item_router = APIRouter()

@item_router.get("/models/{params}")
async def item_by_name(params: str):
    return "Hello world - get models by params" + params
