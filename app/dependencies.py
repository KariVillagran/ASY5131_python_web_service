from fastapi import Header, HTTPException
from datetime import datetime, timedelta
from typing import Optional
from .database import SessionLocal
from .config import settings
import jwt

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm_hash

def decode(token):
    striped_token = token.replace("Bearer ", "")
    return jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])

def encode(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    data["hashed_password"] = ""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encoded_jwt =  jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_db():
    ''' Method for configure database '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_token_header(authorization: str = Header(...)):
    ''' Exemplo of header validation dependency '''
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid authorization header format")
    
    token = authorization.split(" ")[1]
    
    payload = decode(token)    
    username: str = payload.get("username")
    if username == None:
        raise HTTPException(status_code=403, detail="Unauthorized")