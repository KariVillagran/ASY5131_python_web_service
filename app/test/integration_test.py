import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

from app.main import app  # Importa tu instancia de FastAPI desde tu aplicación principal
from app.domain.item import schemas
from ..dependencies import get_token_header

client = TestClient(app)

# Mock de la dependencia get_db para no conectarse a la base de datos real
@pytest.fixture
def mock_get_db():
    with patch("app.dependencies.get_db", return_value=MagicMock()) as mock:
        yield mock

def fake_authenticate():
    print('Fake Authenticated')

app.dependency_overrides[get_token_header] = fake_authenticate

def test_read_main(mock_get_db):
    mock_service = MagicMock()
    with patch("app.domain.item.service.get_item", return_value=schemas.Item(id=1, title="Test Item", description="Test Description", owner_id=1)):
        headers = {"Authorization": "Bearer testtoken"}
        response = client.get("/items/1", headers=headers)
        print(response.json())
        assert response.status_code == 200
        assert response.json() == {"id": 1, "title": "Test Item", "description": "Test Description", "owner_id": 1}

def test_create_item_for_user(mock_get_db):
    mock_service = MagicMock()
    item_data = {"title": "New Item", "description": "New Description"}
    with patch("app.domain.item.service.create_user_item", return_value=schemas.Item(id=1, title="New Item", description="New Description", owner_id=1)):
        headers = {"Authorization": "Bearer testtoken"}
        response = client.post("/items/users/1", json=item_data, headers=headers)
        assert response.status_code == 201
        assert response.json() == {"id": 1, "title": "New Item", "description": "New Description", "owner_id":1}
