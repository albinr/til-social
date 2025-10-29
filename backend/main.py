# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import User, Post

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, TIL Social!"}

@app.get("/posts/")
def read_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts
