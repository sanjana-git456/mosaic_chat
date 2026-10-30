from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    bio: Optional[str] = None
    profile_pic: Optional[str] = None
    class Config:
        from_attributes = True

class Token(BaseModel):
    access: str
    user: UserOut

class LoginRequest(BaseModel):
    username: str
    password: str

class PostBase(BaseModel):
    content_type: str
    content: Optional[str] = None
    media_url: Optional[str] = None
    privacy_level: str

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    author_id: int
    created_at: datetime
    author: UserOut
    class Config:
        from_attributes = True

class BurnoutCheck(BaseModel):
    post_count_last_hour: int
    suggestion: str
    needs_break: bool