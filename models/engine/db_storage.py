#!/usr/bin/env python3
"""This module defines all the methods for interacting with the database"""

from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base, BaseModel
from models.event import Event
from models.user import User
from models.website import Website

# Load environment variables
load_dotenv()

# Retrieve environment variables
username = getenv('DB_USER')
passwd = getenv('DB_PASSWD')
host = getenv('DB_HOST')
db = getenv('DB_NAME')
db_env = getenv('MONITR_ENV')

tables = [User, Website, Event]

class DBStorage():
    """This class represents a database"""

    __engine = None
    __session = None
    
    def __init__(self):
        """Creates an instance of DBStorage"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{username}:{passwd}@{host}/{db}",
            pool_pre_ping=True
        )
        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current db session to retrieve all objects of cls"""

        d = {}
        with self.__session.begin() as session:
            if not cls:
                for table in tables:
                    objs = session.scalars(select(table))
                    for obj in objs:
                        key = f"{obj.__class__.__name__}.{obj.id}"
                        d[key] = obj
            elif cls in classes:
                objs = session.scalars(select(cls))
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    d[key] = obj

            return d

    def new(self, obj):
        """Add the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""

        self.__session.commit()
    
    def delete(self, obj):
        """Delete obj from the current database session"""

        self.__session.delete(obj)

    def reload(self):
        """Creates a database session"""

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )
        self.__session = Session()

    def close(self):
        """Close database session"""
    
        if self.__session:
            self.__session.close()