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

from app import config


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
        config.JWT_SECRET_KEY,
        algorithm=config.JWT_ALGORITHM,
    )


def create_access_token(
    data: dict[str, Any],
) -> str:
    """
    Create an access token.
    """

    return _create_token(
        data=data,
        expires_delta=timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
    )


def create_refresh_token(
    data: dict[str, Any],
) -> str:
    """
    Create a refresh token.
    """

    return _create_token(
        data=data,
        expires_delta=timedelta(
            days=config.REFRESH_TOKEN_EXPIRE_DAYS,
        ),
    )


def decode_token(
    token: str,
) -> dict[str, Any]:
    """
    Decode a JWT token.

    Raises:
        JWTError:
            If the token is invalid.
    """

    return jwt.decode(
        token,
        config.JWT_SECRET_KEY,
        algorithms=[config.JWT_ALGORITHM],
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

    except JWTError:
        return False