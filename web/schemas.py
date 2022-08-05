from datetime import date
from typing import Optional

from pydantic import BaseModel


# properties required during post creation
class PostBase(BaseModel):
    title: str
    description: str
    category: Optional[str]
    author: str


class Post(PostBase):
    class Config:
        orm_mode = True


# properties that appear when client views all posts
class PostView(PostBase):
    view_count: Optional[int]
    date_posted: date

    class Config:
        orm_mode = True


# properties that appear when view individual post
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


# properties that can be changed with put/patch
class UpdatePost(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]

    class Config:
        orm_mode = True
