from fastapi import APIRouter
from text_app.database.database_connection import session
from text_app.database.models import docs
from elastic import ls, index

text_surch_router = APIRouter(
    prefix="/docs",
    tags=["docs"]
)


@text_surch_router.get("/alltexts/{text}")
def get_text(text: str):
    _docs = ls.search(index=index, source={"includes": ["id"]},
                      query={
                          "match":
                              {
                                  "text": text
                              }
                      }
                      , size=20)
    _ids = [document["_source"]["id"] for document in _docs.body["hits"]["hits"]]

    result = session.query(docs) \
        .filter(docs.id.in_(_ids)) \
        .order_by(docs.created_date.desc()) \
        .limit(20)

    return result


@text_surch_router.get("/alltexts")
def get_alltext():
    return [doc for doc in session.query(docs)]


@text_surch_router.delete("/alltexts/{id}")
def get_delete(id: int):
    result = session.query(docs).filter(docs.id == id).delete()
    session.commit()
    ls.delete_by_query(index=index, body={
        "query": {
            "match": {
                "id": id
            }
        }
    }
                       )
    return result
