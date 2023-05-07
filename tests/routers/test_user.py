from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_login_with_valid_credentials():
    response = client.post(
        "/login", json={"email": "admin@gmail.com", "password": "admin"}
    )
    assert response.status_code == 200


def test_login_with_invalid_credentials():
    response = client.post(
        "/login", json={"email": "invalid@gmail.com", "password": "invalid"}
    )
    assert response.status_code == 422
    assert "message" in response.json()


def test_login_with_missing_fields():
    response = client.post("/login", json={"email": "admin@gmail.com"})
    assert response.status_code == 422
    assert "detail" in response.json()
