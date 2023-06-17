from fastapi import APIRouter
from .database.database_connection import session
from .database.models import docs


text_surch_router = APIRouter(
    prefix="/docs",
    tags=["docs"]
)


@text_surch_router.get("/alltexts/{text}")
def get_alltext(text: str):
    return [doc for doc in session.query(docs).filter(docs.texts.like(f"%{text}%"))]