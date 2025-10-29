# create_tables.py
from db import engine, Base
from models import User, Post

Base.metadata.create_all(bind=engine)
print("Tables created!")
