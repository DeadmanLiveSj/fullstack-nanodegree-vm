"""Configuration Code"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import databasesetup
from databasesetup import Base, Restaurant, MenuItem

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

"""Adding new entree to the Restaurant table"""
# firstRestaurant = Restaurant(name="Pizza Place")  # Adding content to the DB
# session.add(firstRestaurant)
# session.commit()

"""Retrieving content in Restaurant table"""
# print(session.query(Restaurant).all())  # Viewing data in the db, In this case all data

"""Adding new entree to the MenuItem table"""
# cheesepizza = MenuItem(name="Cheese Pizza",
#                        description="Mozzarella cheese with chicken",
#                        course="Entree",
#                        price="$8.99",
#                        restaurant=firstRestaurant)
# session.add(cheesepizza)
# session.commit()
# print(session.query(MenuItem).all())

