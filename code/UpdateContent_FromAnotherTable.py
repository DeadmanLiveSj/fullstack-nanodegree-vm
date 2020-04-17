"""Andala's"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import databasesetup
from databasesetup import Base, Restaurant, MenuItem
from prettytable import PrettyTable

"""Initializing the DB"""
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# seeAll = session.query(Restaurant).all()
# for i in seeAll:
#     print(i.name)

tempLine = session.query(Restaurant).filter_by(name="Andala's").one()
"""If we use :-  tempLine = session.query(Restaurant).filter_by(name="Andala's") then we need to iterate through it.
tempLine = session.query(Restaurant).filter_by(name="Andala's").one() will return the value directly"""

thisLine = session.query(MenuItem).filter_by(restaurant_id=tempLine.id)  # Referencing from another table
for i in thisLine:
    print(i.id, i.name)

findRes = session.query(MenuItem).filter_by()