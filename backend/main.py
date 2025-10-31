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

@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPExeption(status_code=404, detail="Post not found")
    return post

@app.post("/auth/register")
def register(username: string, email: string, password: string, db: Session = Depends(get_db)):
    print("register ping")
