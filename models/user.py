"""This module defines the User class"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class represents a User"""

    __tablename__ = 'users'

    name = Column(String(60), nullable=False)
    email = Column(String(100), nullable=False)
    password_hash = Column(String(60), nullable=False)

    websites = relationship('Website', back_populates='user')
