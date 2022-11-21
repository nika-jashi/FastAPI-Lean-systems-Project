from datetime import date
from typing import Optional, List

from pydantic import BaseModel


# properties required during post creation
class PostBase(BaseModel):
    id: int
    title: str
    description: str
    category: str
    view_count: Optional[int]
    date_posted: date


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


# properties that can be changed with put/patch
class UpdatePost(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[PostBase] = []

    class Config:
        orm_mode = True
