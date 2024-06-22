#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base

    Attributes:
        id: Id state
        name: Name of state
    """
    # Linke the class to the crossbasnding table
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)