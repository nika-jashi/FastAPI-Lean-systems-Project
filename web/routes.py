from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from web.schemas import (UpdatePost, PostBase, UserCreate, PostCreate)
from web.views import (create_post,
                       detail_post_view,
                       update_post,
                       destroy_post,
                       get_all_posts,
                       get_hot_posts_view,
                       create_user, get_user_by_email)
from web import database

router = APIRouter(
    tags=['Posts']
)

get_db = database.get_db


@router.get('/', response_model=List[PostBase])
def all(db: Session = Depends(get_db)):
    """ endpoint to view all posts """
    return get_all_posts(db)


@router.post('/create/', status_code=status.HTTP_201_CREATED)
def create_post_for_user(
        user_id: int, post: PostCreate, db: Session = Depends(get_db)
):
    return create_post(db=db, user_id=user_id, post=post)


@router.delete('/delete/{id}/', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    """ endpoint to delete post """
    return destroy_post(id, db)


@router.put('/update/{id}/', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: UpdatePost, db: Session = Depends(get_db)):
    """ endpoint to update post """
    return update_post(id, request, db)


@router.get('/{id}/', status_code=status.HTTP_200_OK, response_model=PostBase)
def show_post(id: int, db: Session = Depends(get_db)):
    """ endpoint to view specific post """
    return detail_post_view(id, db)


@router.get('/top-three/', response_model=List[PostBase])
def get_top_three_posts(db: Session = Depends(get_db)):
    return get_hot_posts_view(db)


@router.post('/user/registration/', status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
