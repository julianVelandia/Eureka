from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

start_router = APIRouter()

templates = Jinja2Templates(directory="internal/platform/templates/startproject")


@start_router.get("/", response_class=HTMLResponse)
async def admin_console(request: Request):
    return templates.TemplateResponse("start_project.html", {"request": request})
