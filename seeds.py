from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///workout_data.db')

Session = sessionmaker(bind=engine)
session = Session()

users = [
    User(),
    User(),
    User()
]

session._bulk_save_objects(users)
session.commit()