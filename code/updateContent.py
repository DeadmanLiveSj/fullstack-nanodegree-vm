"""Assume that we want to update the price of ID : 10 / Item : Veggie Burger / Restaurant : Urban Burger /
Description : Made with freshest of ingredients and home grown spices / Price : $5.99 as $4.99"""

"""Configuration Code"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import databasesetup
from databasesetup import Base, Restaurant, MenuItem
from prettytable import PrettyTable

"""Initializing the DB"""
engine = create_engine('sqlite:///restaurantmenu.db')  # Initializing which db that want to communicate
Base.metadata.bind = engine  # Binding that db to the base. It makes the connection between class definitions and
# their corresponding tables
DBSession = sessionmaker(bind=engine)  # sessionmaker object establish a link of communication between code execution
# and the engine created
"""when doing a CRUD operation to the DB, SQLAlchemy executes db operations via an interface called a session. A session
allows us to write down all the commands we want to executes, but not send them to the db until we call a commit."""
session = DBSession()

"""Finding the item"""
userInput = input("Enter item name : ")
count = 0
t = PrettyTable(['ID','Name','Description','Restaurant Name','Price'])
findResult = session.query(MenuItem).filter_by(name=userInput)  # We can find all rows that contains the given value
# in the selected column

for each in findResult:
    count += 1

if count > 1:
    for item in findResult:
        # print("ID : {0} / Item : {1} / Restaurant : {3} / Description : {2} / Price : {4}".format(each.id,
        #                                          each.name, each.description, each.restaurant.name, each.price))
        t.add_row([item.id, item.name, item.description, item.restaurant.name, item.price])
    print(t)
    idInput = int(input("Enter the ID of the item : "))
    findResult = session.query(MenuItem).filter_by(id=idInput).one()  # When it comes to only one row that could exist
    # in the table with the given parameters, then we can use one() to get that row directly
    newPrice = input("Enter the new price : ")
    findResult.price = newPrice  # updating the value
    session.add(findResult)
    session.commit()
    print("Updated")
    print("ID : {0} / Item : {1} / Restaurant : {3} / Description : {2} / Price : {4}".format(findResult.id,
          findResult.name, findResult.description, findResult.restaurant.name, findResult.price))
elif count == 1:
    findResult = session.query(MenuItem).filter_by(name=userInput).one()
    print("ID : {0} / Item : {1} / Restaurant : {3} / Description : {2} / Price : {4}".format(findResult.id,
          findResult.name, findResult.description, findResult.restaurant.name, findResult.price))
    newPrice = input("Enter the new price : ")
    findResult.price = newPrice
    session.add(findResult)
    session.commit()
    print("Updated")
    print("ID : {0} / Item : {1} / Restaurant : {3} / Description : {2} / Price : {4}".format(findResult.id,
          findResult.name, findResult.description,findResult.restaurant.name, findResult.price))
else:
    print("Not Existing")
