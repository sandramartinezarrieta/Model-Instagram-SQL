import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

Seguidores = Table(
    'followers',
    Base.metadata,
    Column('folower_id',Integer, ForeignKey('user.id')),
    Column('folow_id',Integer, ForeignKey('user.id'))
    )


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=True)
    username = Column(String(250), nullable=False)
    emailname = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)
    following = relationship('follower', secondary= "followers")
    posts = relationship("post", secondary="post")
    comment = relationship("comment", secondary="post")
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'),nullable=False)
    media = relationship("media", secondary="media")


# __tablename__ = ('followers',
#     id_user = Column(String(250), ForeignKey('user.id'),primary_key=True)
#     follow= Column(String(250), ForeignKey('user.id'),primary_key=True)
#     )

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(2500), nullable=False)
    id_author = Column(String(250), ForeignKey('user.id'))
    id_post = Column(String(250), ForeignKey('post.id'))



class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(2500), nullable=False)
    URL = Column(String(2000), nullable=False)
    id_post = Column(String(250), ForeignKey('post.id'))


    

   
    

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')