import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        app.testing = True
        yield client

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {"message": "pong"}

def test_demo(client):
    response = client.get('/demo')
    assert response.status_code == 200
    assert response.json == {"message": "demo"}