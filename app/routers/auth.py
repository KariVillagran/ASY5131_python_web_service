from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..domain.user import service
from ..dependencies import encode

router = APIRouter(tags=["auth"])
security = HTTPBasic()

@router.post("/login/", response_model=dict)
def create_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    db_user = service.get_user_by_email(db, email=credentials.username)
    if db_user and credentials.password == db_user.hashed_password:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"Authorization": "Bearer " + encode(credentials.dict())}