from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///workout_data.db')

Base = declarative_base()

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    workout_name = Column(String)
    difficulty = Column(String)
    started_at = Column(DateTime(), server_default=func.now())
    completed_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f'Workout(id={self.id}, ' + \
            f'workout_name={self.name}, ' + \
            f'difficulty={self.difficulty})'
    



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'name={self.name})'

