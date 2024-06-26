from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

import os

SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(
    os.getenv("DATABASE_URL", SQLALCHEMY_DATABASE_URL)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()