import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user_from = relationship(User, foreign_keys=[user_from_id])
    user_to = relationship(User, foreign_keys=[user_to_id])

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    
    id = Column(Integer, primary_key=True)
    type = Column(Enum("image", "video", name="media_type"), nullable=False)
    url = Column(String(255), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    author = relationship(User)
    post = relationship(Post)

# Generar la base de datos
engine = create_engine('sqlite:///instagram.db')
Base.metadata.create_all(engine)
