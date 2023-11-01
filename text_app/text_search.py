from fastapi import APIRouter
from text_app.database.database_connection import session
from text_app.database.models import docs


text_surch_router = APIRouter(
    prefix="/docs",
    tags=["docs"]
)


@text_surch_router.get("/alltexts/{text}")
def get_text(text: str):
    return [doc for doc in session.query(docs).filter(docs.texts.like(f"%{text}%"))]


@text_surch_router.get("/alltexts")
def get_alltext():
    return [doc for doc in session.query(docs)]

@text_surch_router.delete("/alltexts/{id}")
def get_delete(id: int):
    result = session.query(docs).filter(docs.id == id).delete()
    session.commit()
    return result

