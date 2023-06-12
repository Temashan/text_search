from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/layout")
def get_layout_page(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request})