from app.security import (
    create_access_token,
    decode_token,
)

token = create_access_token(
    {
        "sub": "rajkapoor",
        "user_id": 1,
        "role": "Admin",
    }
)

print(token)

print(decode_token(token))