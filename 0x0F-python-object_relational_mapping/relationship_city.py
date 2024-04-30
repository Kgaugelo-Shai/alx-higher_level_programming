#!/usr/bin/python3
""" This script defines a City class
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): table name of class
        id (int): id of the class
        name (str): name of the class
        state_id (int): state the city belongs
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
