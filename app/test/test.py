from app.security import (
    hash_password,
    verify_password,
)


password = "Raj@123"

hashed = hash_password(password)

print(hashed)

print(
    verify_password(
        "Raj@123",
        hashed,
    )
)

print(
    verify_password(
        "Wrong",
        hashed,
    )
)