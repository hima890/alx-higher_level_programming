#!/usr/bin/python3
"""
Python file that contains the class definition of a Cities and an instance
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base  # Import Base from model_state


class City(Base):
    """
    City class that inherits from Base

    Attributes:
        id: Id state
        name: Name of state
        state_id: Foreign key to states.id
    """
    # Linke the class to the crossbasnding table
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
