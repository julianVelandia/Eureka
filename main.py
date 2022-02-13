from fastapi import FastAPI
from src.app.routers.information import information_router

app = FastAPI()

app.include_router(information_router)
