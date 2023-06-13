from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date

metadata = MetaData()

docs = Table(
    "docs",
    metadata,
    Column("id", Integer, nullable=False, autoincrement=True),
    Column("rubrics", String, nullable=False),
    Column("texts", String, nullable=False),
    Column("created_date", Date, nullable=False)
)