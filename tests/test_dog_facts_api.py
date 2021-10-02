from fastapi.testclient import TestClient

from dog_facts_api import __version__
from dog_facts_api.main import create_app

client = TestClient(create_app())


def test_home():
    response = client.get("/")
    assert response.status_code == 200
