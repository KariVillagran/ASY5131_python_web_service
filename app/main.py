from fastapi import FastAPI
from app.routers import items, users, auth
from app.database import engine, SessionLocal, Base

## Generate database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)
app.include_router(auth.router)