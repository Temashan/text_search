from fastapi import FastAPI, Request
from .text_search import text_surch_router as router_pages
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from text_app import templates

app = FastAPI(
    title="Text search app"
)

app.include_router(router_pages)
app.mount('/static', StaticFiles(directory='text_app/templates/text_app'))
_templates = Jinja2Templates(directory='text_app/templates/text_app')

@app.get("/")
def home(request: Request):
    return _templates.TemplateResponse('layout.html', context={"request": request})


# origins = [
#     "http://localhost:8000"
# ]

# templates = Jinja2Templates(directory="/templates/text_app")
#
# @app.get("/")
# async def read_root(request: Request):
#     return templates.TemplateResponse("layout.html", {"request": request})
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credential=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["*"],
# )
