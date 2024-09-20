#!/usr/bin/env python3
"""This module defines the baseModel class"""
import uuid
from datetime import datetime
import models
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, String


class Base(DeclarativeBase):
    pass

class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes instance of a class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()

        else:
            for key, value in kwargs.items():
                if key not in ('created_at', '__class__'):
                    setattr(self, key, value)

            # Ensure 'created_at' exists in kwargs before converting
            if 'created_at' in kwargs:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            else:
                self.created_at = datetime.utcnow()  # Set current time if not provided

            # Ensure 'id' exists, generate if missing
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())



    def __str__(self):
        """return string representation of t object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save changes to storage"""

        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing \
all keys/values of __dict__ of the instance"""

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict.pop('_sa_instance_state', None)
        return new_dict
