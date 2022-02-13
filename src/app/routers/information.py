from fastapi import APIRouter

information_router = APIRouter()

@information_router.get("/information/{params}")
async def information_by_name(params: str):
    return "Hello world - get information by params" + params
