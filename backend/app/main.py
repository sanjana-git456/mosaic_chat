from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, posts
from .config import settings
from .dependencies import get_current_user
from . import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")
app.include_router(posts.router, prefix="/api")

@app.get("/api/auth/me/", response_model=schemas.UserOut)
def get_me(user: schemas.UserOut = Depends(get_current_user)):
    return user

@app.get("/")
def root():
    return {"message": "MosaicChat API is running"}