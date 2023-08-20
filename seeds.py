from models import User, Workout, Exercise
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

workouts = [
    Workout(
        workout_name=fake.name()

    )
for i in range(50)
]

session.add_all(workouts)
session.commit()

exercises = [
    Exercise(
        exercise_name=fake.name()
    )
for i in range(100)
]

session.add_all(exercises)
session.commit()