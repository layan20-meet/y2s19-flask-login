from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,secret_word):
    """Add a user to the DB."""
    user = User(username=name)
    session.add(user)
    user.hash_password(secret_word)
    session.commit()

def get_user(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()

def fav_food(food, username):
	get_user(username).fav_food=food
	session.commit()

