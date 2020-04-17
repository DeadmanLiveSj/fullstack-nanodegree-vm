from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import databasesetup
from databasesetup import Base, Restaurant, MenuItem

"""Initializing the DB"""
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

"""finding the row"""
findRes = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()

"""deleting the row"""
session.delete(findRes)
session.commit()


"""Just checking again whether it is deleted"""
checkAgain = session.query(MenuItem).filter_by(name='Spinach Ice Cream')
for i in checkAgain:
    print(i.id, i.name)