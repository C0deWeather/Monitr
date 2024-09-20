"""This module defines the Website class"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Website(BaseModel, Base):
    """This class represents a website"""

    __tablename__ = 'websites'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)

    user = relationship('User', back_populates='websites')
    events = relationship('Event', back_populates='website')
