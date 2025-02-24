import pytest
from fastapi.testclient import TestClient
from app.routes import app

@pytest.fixture
def client():
    return TestClient(app)

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_demo(client):
    response = client.get('/demo')
    assert response.status_code == 200
    assert response.json() == {"message": "demo"}