import sqlalchemy
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date, Text

metadata = MetaData()

docs = Table(
    "docs",
    metadata,
    Column("id", Integer, nullable=False, autoincrement=True),
    Column("rubrics", String(45), nullable=False),
    Column("texts", Text, nullable=False),
    Column("created_date", Date, nullable=False)
)

