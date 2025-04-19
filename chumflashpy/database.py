from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATABASE_URL = "postgresql+psycopg2://postgres:Mehdi%401362@localhost:5432/chumflashpy"
engine = create_engine(DATABASE_URL)


def create_tables():
    Base.metadata.create_all(engine)
