import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'folower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(String(250), nullable=False)
    user_to_id = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250),nullable=False)
    firstname = Column(String(250),nullable=False)
    lastname= Column(String(250), nullable=False)
    email= Column(String(250), nullable=False)
    follower = relationship('Follower', backref='user', lazy=True)
    comment = relationship('User', backref='user', lazy=True)
    post = relationship('Post', backref='user', lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250),nullable=False)
    author_id = Column(String(250),nullable=False)
    post_id = Column(String(250),nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'),
        nullable=False)
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250),nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    comment = relationship('Comment', backref='comment', lazy=True)
    media = relationship('Media', backref='media', lazy=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type= Column(String(250),nullable=False)
    url = Column(String(250),nullable=False)
    post_id = Column(String(250),nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'),
        nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
