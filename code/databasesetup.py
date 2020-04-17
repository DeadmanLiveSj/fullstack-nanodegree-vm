"""Configuration Code"""
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


"""Class Definition"""
class Restaurant (Base):  # Table 1
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


"""Class Definition"""
class MenuItem (Base):  # Table 2
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


"""End Configuration Code"""
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
