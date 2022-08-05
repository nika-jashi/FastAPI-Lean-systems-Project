import datetime

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from web.models import Posts
from web.schemas import UpdatePost, Post
from web.database import get_db


def get_all_posts(db: Session):
    """ View that lists all post """
    all_posts = []
    for post in db.query(Posts):
        if post is None:
            continue
        all_posts.append(post)
    return all_posts


def create_post(request: Post, db: Session = Depends(get_db)):
    """ View that creates post """
    new_post = Posts(title=request.title,
                     description=request.description,
                     category=request.category,
                     author=request.author,
                     date_posted=datetime.datetime.now())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def destroy_post(id: int, db):
    """ View which ensures the deletion of a specific post """
    selected_post = db.get(Posts, id)
    if not selected_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(selected_post)
    db.commit()
    return {"ok": "Deleted Successfully"}


def update_post(id: int, request: UpdatePost, db: Session = Depends(get_db)):
    """ View which provides update of a specific post """

    post = db.query(Posts).filter(Posts.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} not found and cannot be updated')
    post.update(request.dict())
    db.commit()
    return {'updated_post': request}


def detail_post_view(id: int, db: Session = Depends(get_db)):
    """ View where you can get specific post by id """
    specific_post = db.query(Posts).filter(Posts.id == id).first()
    if not specific_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id {id} is not available")
    view = []
    for initial_views in db.query(Posts.view_count).filter(Posts.id == id).first():
        view.append(initial_views + 1)
    db.query(Posts).filter(Posts.id == id).update({"view_count": view[0]})
    db.commit()
    return specific_post


def get_top_three_posts_view(db: Session):
    """ View for three the most popular posts"""
    all_posts = []
    for post in db.query(Posts).order_by(Posts.view_count.desc()):
        if post is None:
            continue
        all_posts.append(post)

    return all_posts[0:3]
