import pytest
from app import app

@pytest.fixture
def test_app():
    yield app

@pytest.fixture
def client(test_app):
    return test_app.test_client()

def test_index_returns_200(client):
    res = client.get("/")
    assert res.status_code == 200