from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

admin_router = APIRouter()

templates = Jinja2Templates(directory="internal/platform/templates/admin")


@admin_router.get("/admin", response_class=HTMLResponse)
async def admin_console(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request, "test": "Admin console"})
