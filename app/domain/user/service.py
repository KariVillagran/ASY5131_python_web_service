from sqlalchemy.orm import Session
# TODO: agregar repository user
from . import repository, schemas


def get_user(db: Session, user_id: int):
    return repository.get_user(db=db, user_id=user_id)

def get_user_by_email(db: Session, email: str):
    return repository.get_user_by_email(db=db, email=email)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_users(db=db)

def create_user(db: Session, user: schemas.UserCreate):
    return repository.create_user(db=db, user=user)

