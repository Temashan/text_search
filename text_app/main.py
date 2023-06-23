from fastapi import FastAPI, Request, Body, Depends
from mysqlx import Session
from starlette.responses import JSONResponse

from text_app.database.database_connection import s
from text_app.database.models import docs
from text_app.text_search import text_surch_router as router_pages
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles


app = FastAPI(
    title="Text search app"
)

def get_db():
    db = s()
    try:
        yield db
    finally:
        db.close()

app.include_router(router_pages)
app.mount('/static', StaticFiles(directory='text_app/templates/text_app', html=True))
_templates = Jinja2Templates(directory='text_app/templates/text_app')
_static = Jinja2Templates(directory='text_app/static')

@app.get("/")
def home(request: Request):
    return _templates.TemplateResponse('layout.html', context={"request": request})

@app.post("/hello")
async def hello(data=Body()):
    text = docs(rubrics=data["rubrics"], texts=data["texts"], created_date=data["created_date"] )
    db = s()
    db.add(text)
    db.commit()
    return {"message": "Данные успешно сохранены в базе данных."}


@app.delete("/alltexts/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    person = db.query(docs).filter(docs.id == id).first()

    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    db.delete(person)
    db.commit()
    return person

