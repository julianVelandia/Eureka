from fastapi import FastAPI
from src.app.routers.item import item_router

app = FastAPI()

app.include_router(item_router)
