"""This module defines the Event class"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String, Text
from sqlalchemy.orm import relationship


class Event(BaseModel, Base):
    """This class represents an event"""

    __tablename__ = "events"

    website_id = Column(String(60), ForeignKey('websites.id'), nullable=False)
    event_type = Column(String(50), nullable=False)
    event_data = Column(Text, nullable=False)

    website = relationship('Website', back_populates='events')
