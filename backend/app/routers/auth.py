from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, security, database

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register/", response_model=schemas.Token, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = crud.create_user(db, user)
    access_token = security.create_access_token(subject=new_user.username)
    return {"access": access_token, "user": new_user}

@router.post("/login/", response_model=schemas.Token)
def login(req: schemas.LoginRequest, db: Session = Depends(database.get_db)):
    user = crud.get_user_by_username(db, username=req.username)
    if not user or not security.verify_password(req.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = security.create_access_token(subject=user.username)
    return {"access": access_token, "user": user}

@router.get("/me/", response_model=schemas.UserOut)
def read_users_me(current_user: schemas.UserOut = Depends(lambda: None)):
    # Injected via dependency in main app routing
    return current_user