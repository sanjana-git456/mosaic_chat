from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database, dependencies

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user = Depends(dependencies.get_current_user)):
    return crud.create_post(db, post, user_id=current_user.id)

@router.get("/", response_model=List[schemas.PostOut])
def read_posts(db: Session = Depends(database.get_db), current_user = Depends(dependencies.get_current_user)):
    return crud.get_posts(db)

@router.get("/burnout/", response_model=schemas.BurnoutCheck)
def check_burnout(db: Session = Depends(database.get_db), current_user = Depends(dependencies.get_current_user)):
    count = crud.get_user_post_count_recent(db, current_user.id)
    needs_break = count > 5
    suggestion = "Keep creating!" if not needs_break else "You've been busy! How about a 10-minute mindfulness break?"
    return {"post_count_last_hour": count, "suggestion": suggestion, "needs_break": needs_break}