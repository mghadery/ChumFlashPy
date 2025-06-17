from database import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class FlashCard(Base):
    __tablename__ = "flash_cards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    front = Column(String(1000), nullable=False)
    back = Column(String(1000), nullable=False)
    tags = Column(String(500), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    categories = relationship("Category")
    front_lang = Column(String(10), nullable=True)
    back_lang = Column(String(10), nullable=True)
    last_practiced = Column(DateTime)
    creation_at = Column(
        DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc)
    )
    complexity = Column(Integer, nullable=False)
    username = Column(String(100), nullable=False)

    # def __init__(
    #     self, id, front, back, tags, category_id, last_practiced, creation_at, username
    # ):
    #     self.id = id
    #     self.front = front
    #     self.back = back
    #     self.tags = tags
    #     self.category_id = category_id
    #     self.last_practiced = last_practiced
    #     self.creation_at = creation_at
    #     self.username = username

    def __str__(self):
        return f"id: {self.id}\nfront: {self.front}\nback: {self.back}\ntags: {self.tags}\nfront_lang: {self.front_lang}\nback_lang: {self.back_lang}\ncomplexity:{self.complexity}"
