from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

eninge = create_engine('sqlite:///workout_data.db')