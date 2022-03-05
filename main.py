from fastapi import FastAPI

from src.app.routers.admin import admin_router
from src.app.routers.information import information_router
from src.app.routers.start import start_router

app = FastAPI()

app.include_router(information_router)
app.include_router(admin_router)
app.include_router(start_router)


