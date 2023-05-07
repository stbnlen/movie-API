import pytest
from utils.jwt_manager import create_token
from jwt import decode, InvalidTokenError


def test_create_token():
    # Test with valid data
    data = {"user_id": 1, "username": "test_user"}
    token = create_token(data)
    decoded_token = decode(token, key="my_secret_key", algorithms=["HS256"])
    assert decoded_token == data


def test_create_token_invalid_data():
    # Test with invalid data (non-dict)
    data = "invalid_data"
    with pytest.raises(ValueError):
        create_token(data)


def test_create_token_invalid_key():
    # Test with invalid key
    data = {"user_id": 1, "username": "test_user"}
    with pytest.raises(InvalidTokenError):
        token = create_token(data)
        decoded_token = decode(token, key="my_key", algorithms=["HS256"])
