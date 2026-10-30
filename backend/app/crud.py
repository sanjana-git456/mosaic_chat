from sqlalchemy.orm import Session
from . import models, schemas, security
from datetime import datetime, timedelta

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = security.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.model_dump(), author_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).order_by(models.Post.created_at.desc()).offset(skip).limit(limit).all()

def get_user_post_count_recent(db: Session, user_id: int):
    one_hour_ago = datetime.utcnow() - timedelta(hours=1)
    return db.query(models.Post).filter(
        models.Post.author_id == user_id,
        models.Post.created_at >= one_hour_ago
    ).count()