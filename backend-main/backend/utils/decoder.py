import jwt
import os
secret_key_router = os.getenv("PRIVATE_fastapi_token")

# jwt.encode({"user_id": row[0], "email": row[1]}, key=secret_key_router, algorithm="HS256"))

def decode_token(token: str) -> dict["user_id": int, "email": str]:
    return jwt.decode(token, secret_key_router, algorithms=["HS256"])


def encode_token(user_id:int, email:str) -> str:
    return jwt.encode({"user_id": user_id, "email": email}, key=secret_key_router, algorithm="HS256")