from fastapi.responses import FileResponse
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from pages.router import router as router_pages

app = FastAPI(
    title="Text search app"
)

doc = [
    {'id': 1, 'rubrics': 'sport', 'text': 'Messi is going to play in the USA', 'created_date': '2023-06-09'},
    {'id': 2, 'rubrics': 'news', 'text': 'Fire was in Minsk', 'created_date': '2023-06-09' },
    {'id': 3, 'rubrics': 'about animals', 'text': 'Bear was seen in Molodechno', 'created_date': '2023-06-09'},
    {'id': 4, 'rubrics': 'politics', 'text': 'Trump is running for president', 'created_date': '2023-06-09'},
    {'id': 5, 'rubrics': 'economics', 'text': 'Belarusian economy has fallen over the past 2 month', 'created_date': '2023-06-08'},
    {'id': 6, 'rubrics': 'technologies', 'text': 'Good apple presentation was 2 days ago', 'created_date': '2023-06-08'},
    {'id': 7, 'rubrics': 'cars', 'text': 'New electro BMW7 comes to Belarus', 'created_date': '2023-06-08'}
]

@app.get("/")
def text():
    return doc


@app.get("/doc/{text}")
def find_text(text: str):
    return [doc for doc in doc if text in doc["text"]]

class Text(BaseModel):
    id: int
    rubrics: str
    text: str
    created_date: datetime

app.include_router(router_pages)


