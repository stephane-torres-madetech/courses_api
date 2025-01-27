import pytest
from app import app
from db import Database
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

def test_db_connection_is_not_null():
    db = Database()
    assert db.connection
    db.close_connection()
    assert db.connection.closed


# def test_db_query_is_not_null():
#     conn = connect_to_db()
