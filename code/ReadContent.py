"""Configuration Code"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import databasesetup
from databasesetup import Base, Restaurant, MenuItem
from prettytable import PrettyTable  # Library for display outputs in a table

"""Initializing the DB"""
engine = create_engine('sqlite:///restaurantmenu.db')  # Initializing which db that want to communicate
Base.metadata.bind = engine  # Binding that db to the base. It makes the connection between class definitions and
# their corresponding tables
DBSession = sessionmaker(bind=engine)  # sessionmaker object establish a link of communication between code execution
# and the engine created
"""when doing a CRUD operation to the DB, SQLAlchemy executes db operations via an interface called a session. A session
allows us to write down all the commands we want to executes, but not send them to the db until we call a commit."""
session = DBSession()  # The DBSession object gives a staging zone for all of the objects loaded into
# a db session object. Any change made to thw objects in the session won't be persisted into the db,
# until call session.commit

# firstResult = session.query(Restaurant).first()
# print(firstResult.name)

# items = session.query(Restaurant).all()
# for i in items:
#     print(i.name)

# for i in session.query(Restaurant).all():
#     print(i.id, i.name)

# for i in session.query(MenuItem).all():
#     print(i.id, i.name, i.course, i.description, i.price, i.restaurant_id)

"""Read content and display it in a table"""
t = PrettyTable(['ID','Name','Description','Restaurant Name','Price'])
for item in session.query(MenuItem).all():
    t.add_row([item.id, item.name, item.description, item.restaurant.name, item.price])
print(t)
