from jwt import encode, decode


def create_token(data: dict):
    try:
        token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
        return token
    except Exception as e:
        raise ValueError("Error creating token: {}".format(str(e)))


def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=["HS256"])
    return data
