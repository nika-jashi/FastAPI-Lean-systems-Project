from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from web.database import Base


class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    category = Column(String)
    date_posted = Column(DateTime)
    view_count = Column(Integer, default=0)

    author = relationship("User", back_populates="articles")

    author_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return self.title


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    articles = relationship("Posts", back_populates="author")

    def __repr__(self):
        return self.email
