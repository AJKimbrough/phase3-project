from models import User
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from faker import Faker

engine = create_engine('sqlite:///workout_data.db')

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

users = [
    User(
        user_name=fake.name()
    )
for i in range(20)
]

session.add_all(users)
session.commit()