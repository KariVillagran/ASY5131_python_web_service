from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import repository, schemas
from ...resources.strings import ITEM_DOES_NOT_EXIST_ERROR


def create_user_item(db: Session, item: schemas.ItemCreate, user_id=int):
    return repository.create_user_item(db, item, user_id);

def get_item(db: Session, item_id: int):
    db_item = repository.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
    return repository.get_item(db, item_id);

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_items(db, skip, limit);

def remove_item(db: Session, item_id: int):
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
    return repository.remove_item(db, db_item)