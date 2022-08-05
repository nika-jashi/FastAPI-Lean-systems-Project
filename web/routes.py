from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from web.schemas import (UpdatePost, ShowPost, PostView, Post)
from web.views import (create_post,
                       detail_post_view,
                       update_post,
                       destroy_post,
                       get_all_posts,
                       get_top_three_posts_view)
from web import database

router = APIRouter(
    tags=['Posts']
)

get_db = database.get_db


@router.get('/', response_model=List[PostView])
def all(db: Session = Depends(get_db)):
    """ endpoint to view all posts """
    return get_all_posts(db)


@router.post('/create/', status_code=status.HTTP_201_CREATED)
def create(request: Post, db: Session = Depends(get_db)):
    """ endpoint to create post """
    return create_post(request, db)


@router.delete('/delete/{id}/', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    """ endpoint to delete post """
    return destroy_post(id, db)


@router.put('/update/{id}/', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: UpdatePost, db: Session = Depends(get_db)):
    """ endpoint to update post """
    return update_post(id, request, db)


@router.get('/{id}/', status_code=status.HTTP_200_OK, response_model=ShowPost)
def show_post(id: int, db: Session = Depends(get_db)):
    """ endpoint to view specific post """
    return detail_post_view(id, db)


@router.get('/top-three/', response_model=List[PostView])
def get_top_three_posts(db: Session = Depends(get_db)):
    return get_top_three_posts_view(db)
