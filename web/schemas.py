from datetime import date
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str
    category: Optional[str]
    author: str


class Post(PostBase):
    class Config:
        orm_mode = True


class PostView(PostBase):
    view_count: Optional[int]
    date_posted: date

    class Config:
        orm_mode = True


class ShowPost(BaseModel):
    id: int
    title: str
    description: str
    category: str
    author: str
    view_count: Optional[int]
    date_posted: date

    class Config:
        orm_mode = True


class UpdatePost(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]

    class Config:
        orm_mode = True
