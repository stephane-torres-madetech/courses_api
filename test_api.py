import pytest
from app import app
import json

@pytest.fixture
def test_app():
    yield app

@pytest.fixture
def client(test_app):
    return test_app.test_client()

def test_index_returns_200(client):
    res = client.get("/")
    assert res.status_code == 200

def test_index_returns_json_data(client):
    res = client.get("/")
    assert True if json.loads(res.data) else False