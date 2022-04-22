from fastapi.testclient import TestClient

from app import __version__
from app.main import create_app

client = TestClient(create_app())


def test_home():
    response = client.get("/")
    assert response.status_code == 200
