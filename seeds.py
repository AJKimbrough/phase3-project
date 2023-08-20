from models import User
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from faker import Faker

engine = create_engine('sqlite:///workout_data.db')

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

users = [
    User(),
    User(),
    User()
]

session._bulk_save_objects(users)
session.commit()