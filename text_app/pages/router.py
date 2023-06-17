from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)


# @router.get("/layout")
# def get_layout_page(request: Request):
#     templates = Jinja2Templates(directory="templates")
#     return templates.TemplateResponse("layout.html", {"request": request})
#
