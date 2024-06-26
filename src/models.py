import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """

class User_private(Base):
    __tablename__='User Private'
    user_private_id= Column(Integer, primary_key=True)
    user_name=Column(String(15), nullable=False, unique= True)
    password=Column(String(15), nullable=False)
    email= Column(String(20), nullable=False, unique=True)


class User_public (Base):
    __tablename__='User Public'
    user_public_id= Column(Integer, primary_key=True)
    user_name=Column(String(15), nullable=False, unique= True)
    description = Column(String(250), nullable=True, unique=True)
    user_private_id = Column(Integer, ForeignKey(User_private.user_private_id))

class Multimedia (Base):
    __tablename__='Multimedia'
    multimedia_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User_public.user_public_id))
    media= Column(String(250), nullable= False) 

class Images (Base):
    __tablename__='Images'
    images_id = Column(Integer, primary_key=True)
    profile_photo = Column(Boolean)  # Checking if the image is a profile image then its True and show the image and shows nothing if False
    multimedia_id = Column(Integer, ForeignKey(Multimedia.multimedia_id))
    user_public_id=Column(Integer, ForeignKey(User_public.user_public_id))

class Post (Base):
    __tablename__='Post'
    post_id= Column(Integer, primary_key=True)
    user_public_id=Column(Integer, ForeignKey(User_public.user_public_id))
    image_id = Column(Integer, ForeignKey(Images.images_id)) 
    post = Column(Enum, nullable=False)


class Likes(Base):
    __tablename__='Likes'
    like_id=Column(Integer, primary_key=True)
    likes= Column(Integer, nullable=True)
    post_id = Column(Integer, ForeignKey(Post.post_id))
    user_liking_id = Column (Integer, ForeignKey(User_public.user_public_id))
class Coments(Base):
    __tablename__='Coments'
    coment_id= Column(Integer, primary_key=True)
    coment= Column(String(250), nullable=True)
    post_id= Column(Integer, ForeignKey(Post.post_id))
    user_commenting_id = Column (Integer, ForeignKey(User_public.user_public_id))

class Feed (Base):
    __tablename__='Feed'  
    feed_id=Column(Integer, primary_key=True)
    user_public_id= Column(Integer, ForeignKey(User_public.user_public_id))
    post= Column(String, unique=True)
    post_id =Column(Integer, ForeignKey(Post.post_id))

class Followers (Base):
    __tablename__='Followers'
    follower_id= Column(Integer, primary_key=True)
    user_followers=Column(Integer, ForeignKey(User_public.user_public_id))
    user_following=Column(Integer, ForeignKey(User_public.user_public_id))

class DMs (Base):
    __tablename__='DMs'
    dms_id= Column(Integer, primary_key=True)
    user_reciver_id=Column(Integer, ForeignKey(User_public.user_public_id))
    user_sending_id=Column(Integer, ForeignKey(User_public.user_public_id))
    dm= Column(String(250), nullable=False, unique=True)

class Stories(Base):
    __tablename__='Stories'
    storie_id= Column(Integer, primary_key=True)
    user_public_id=Column(Integer, ForeignKey(User_public.user_public_id))
    image_id = Column(Integer, ForeignKey(Images.images_id))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
