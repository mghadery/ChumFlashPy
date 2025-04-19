from sqlalchemy import Column, String, Integer
from database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name
