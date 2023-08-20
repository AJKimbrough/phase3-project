from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite:///workout_data.db')

Base = declarative_base()

athlete = Table(
    'athletes',
    Base.metadata,
    Column('workout_id', ForeignKey('workouts.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    extend_existing=True,
)

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    workout_name = Column(String)
    difficulty = Column(String)
    started_at = Column(DateTime(), server_default=func.now())
    completed_at = Column(DateTime(), onupdate=func.now())

    users = relationship('User', secondary=athlete, back_populates='workouts')

    def __repr__(self):
        return f'Workout(id={self.id}, ' + \
            f'workout_name={self.name}, ' + \
            f'difficulty={self.difficulty})'
    

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    exercise_type = Column(String)
    
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'Exercise(id={self.id}, ' + \
            f'exercise_name={self.exercise_name}, ' + \
            f'exercise_type={self.exercise_type})'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)

    exercises = relationship('Exercise', backref=backref('user'))

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'name={self.name})'

