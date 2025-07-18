from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, database

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    user = models.User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
