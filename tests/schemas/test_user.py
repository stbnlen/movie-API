from pydantic import ValidationError
from schemas.user import User


def test_create_user():
    user_data = {"email": "example@example.com", "password": "examplepassword"}
    user = User(**user_data)
    assert user.email == user_data["email"]
    assert user.password == user_data["password"]


def test_create_user_with_optional_field():
    user_data = {
        "email": "example@example.com",
        "password": "examplepassword",
    }
    user = User(**user_data)
    assert user.email == user_data["email"]
    assert user.password == user_data["password"]


def test_create_user_with_invalid_data():
    user_data = {"email": "example", "password": "short"}
    try:
        user = User(**user_data)
    except ValidationError as e:
        assert "value_error.email" in e.errors()
        assert "value_error.any_str.min_length" in e.errors()["email"][0]["msg"]
        assert "value_error.password.min_length" in e.errors()["password"][0]["msg"]
