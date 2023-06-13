from fastapi.responses import FileResponse
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from pages.router import router as router_pages
from database import connection

app = FastAPI(
    title="Text search app"
)

@app.get("/texts")
def get_text():
    db_connection = connection.create_connection()
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM docs")
    result = cursor.fetchall()

    # Формируем список словарей с результатами
    docs = []
    for row in result:
        user = {
            "id": row[0],
            "rubrics": row[1],
            "texts": row[2],
            "created_date": row[3]
        }
        docs.append(user)

    cursor.close()
    db_connection.close()

    return {"docs": docs}


