from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .database import Base

class ContentType(enum.Enum):
    TEXT = "text"
    IMAGE = "image"
    VOICE = "voice"
    VIDEO = "video"

class PrivacyLevel(enum.Enum):
    PRIVATE = "private"
    FRIENDS = "friends"
    FOLLOWERS = "followers"
    PUBLIC = "public"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    bio = Column(Text, nullable=True)
    profile_pic = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    posts = relationship("Post", back_populates="author")
    subscriptions = relationship("Subscription", foreign_keys="Subscription.creator_id")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    content_type = Column(String, default="text")
    content = Column(Text, nullable=True)
    media_url = Column(String, nullable=True)
    privacy_level = Column(String, default="public")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    author = relationship("User", back_populates="posts")

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    subscriber_id = Column(Integer, ForeignKey("users.id"))
    creator_id = Column(Integer, ForeignKey("users.id"))
    tier_name = Column(String)
    price = Column(Float)
    active = Column(DateTime(timezone=True), server_default=func.now())