from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from ..dependencies import get_token_header, get_db
from ..domain.item import service, schemas


router = APIRouter(
  prefix="/items",
  tags=["items"],
  dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

@router.get("/{item_id}", response_model=schemas.Item, status_code=200)
async def read_main(item_id: str, db: Session = Depends(get_db)):
    print(item_id)
    return service.get_item(db=db, item_id=item_id)

@router.post("/users/{user_id}", response_model=schemas.Item, status_code=201)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return service.create_user_item(db=db, item=item, user_id=user_id)