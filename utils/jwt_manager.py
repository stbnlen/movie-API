import os
from jwt import encode, decode

SECRET_KEY = os.getenv("SECRET_KEY")


def create_token(data: dict) -> str:
    try:
        token: str = encode(payload=data, key=SECRET_KEY, algorithm="HS256")
        return token
    except Exception as e:
        raise ValueError("Error creating token: {}".format(str(e)))


def validate_token(token: str) -> dict:
    data: dict = decode(token, key=SECRET_KEY, algorithms=["HS256"])
    return data
