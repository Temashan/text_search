from sqlalchemy import Column
from sqlalchemy import Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class docs(Base):
    __tablename__ = "textsearch"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rubrics = Column(String(45), nullable=False)
    texts = Column(Text, nullable=False)
    created_date = Column(Date, nullable=False)

metadata = Base.metadata
