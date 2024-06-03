import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..domain.user import models, schemas
from ..domain.user.repository import get_user, get_user_by_email, get_users, create_user

# Configurar la base de datos en memoria para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base de datos y las tablas
models.Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db() -> Session:
    # Crear una sesión de base de datos para pruebas
    session = TestingSessionLocal()
    yield session
    session.close()

def test_create_user(db):
    user_data = schemas.UserCreate(email="test@example.com", password="password")
    user = create_user(db, user_data)
    assert user.email == "test@example.com"
    assert user.hashed_password == "passwordnotreallyhashed"

def test_get_user(db):
    user_data = schemas.UserCreate(email="test2@example.com", password="password")
    user = create_user(db, user_data)
    fetched_user = get_user(db, user.id)
    assert fetched_user
    assert fetched_user.email == "test2@example.com"

def test_get_user_by_email(db):
    user_data = schemas.UserCreate(email="test3@example.com", password="password")
    user = create_user(db, user_data)
    fetched_user = get_user_by_email(db, "test3@example.com")
    assert fetched_user
    assert fetched_user.email == "test3@example.com"

def test_get_users(db):
    user_data1 = schemas.UserCreate(email="user1@example.com", password="password")
    user_data2 = schemas.UserCreate(email="user2@example.com", password="password")
    create_user(db, user_data1)
    create_user(db, user_data2)
    users = get_users(db, skip=0, limit=10)
    assert len(users) >= 2
    emails = [user.email for user in users]
    assert "user1@example.com" in emails
    assert "user2@example.com" in emails
