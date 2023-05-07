from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == b"<h1>Hello world</h1>"


def test_home_returns_hello_world():
    with TestClient(app) as client:
        response = client.get("/")
        assert "Hello world" in str(response.content)


def test_home_returns_html():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.content == b"<h1>Hello world</h1>"
