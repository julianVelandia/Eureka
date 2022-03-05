from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.handler.getinformationbyconfig.contract.request import Params
from src.handler.getinformationbyconfig.handler import Handler as HandlerInformationByConfig

information_router = APIRouter()

templates = Jinja2Templates(directory="internal/platform/templates/startproject")


@information_router.get("/information/config/{language}/{config_name}", response_class=HTMLResponse)
async def information_by_config(request: Request, language: str, config_name: str):
    params = Params(language, config_name)
    handler_response = HandlerInformationByConfig().handler(params)
    return templates.TemplateResponse("show_information.html", {"request": request, "response": handler_response})
