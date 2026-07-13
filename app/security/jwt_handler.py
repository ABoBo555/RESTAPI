from datetime import (
    datetime,
    timedelta,
    timezone,
)
from typing import Any

from jose import (
    JWTError,
    jwt,
)

from app.constants import *

from app.schemas.user_schemas import (
    TokenPayload,
)

from uuid import uuid4

def _create_token(
    data: dict[str, Any],
    expires_delta: timedelta,
) -> str:
    """
    Create a JWT token.
    """

    payload = data.copy()

    payload["exp"] = (
        datetime.now(timezone.utc) + expires_delta
    )

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def create_access_token(
    user_id: int,
    username: str,
    role: str,
) -> str:
    """
    Create a signed JWT access token.
    """

    return _create_token(
        data={
            "jti": str(uuid4()),
            "sub": username,
            "user_id": user_id,
            "role": role,
            "type": "access",
        },
        expires_delta=timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
    )

def create_refresh_token(
    user_id: int,
    username: str,
    role: str,
) -> str:
    """
    Create a signed JWT refresh token.
    """

    return _create_token(
        data={
            "jti": str(uuid4()),
            "sub": username,
            "user_id": user_id,
            "role": role,
            "type": "refresh",
        },
        expires_delta=timedelta(
            days=REFRESH_TOKEN_EXPIRE_DAYS,
        ),
    )


def verify_token(
    token: str,
) -> bool:
    """
    Verify whether a JWT token is valid.
    """

    try:
        decode_token(token)
        return True

    except Exception:
        return False
    

def decode_token(
    token: str,
) -> TokenPayload:
    """
    Decode a JWT and return the payload.
    """

    payload = jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[
            JWT_ALGORITHM,
        ],
    )

    return TokenPayload.model_validate(
        payload,
    )