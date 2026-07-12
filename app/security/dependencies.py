from jose import JWTError

from fastapi import (
    Depends,
)

from fastapi.security import OAuth2PasswordBearer

from app.exceptions import (
    InvalidTokenError,
    PermissionDeniedError,
)

from app.security import (
    decode_token,
)

from collections.abc import Callable

from app.schemas.user_schemas import (
    TokenPayload,
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login",
)


def require_roles(
    *roles: str,
) -> Callable:
    """
    Require one of the specified roles.
    """

    def role_checker(
        current_user: TokenPayload = Depends(
            get_current_active_user,
        ),
    ) -> TokenPayload:

        if current_user.role not in roles:
            raise PermissionDeniedError(
                "You do not have permission to perform this action."
            )

        return current_user

    return role_checker


def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> TokenPayload:
    """
    Validate a JWT and return its payload.
    """

    try:
        return decode_token(token)

    except JWTError:
        raise InvalidTokenError(
            "Invalid or expired access token."
        )


def get_current_active_user(
    current_user: TokenPayload = Depends(
        get_current_user,
    ),
) -> TokenPayload:
    """
    Return the authenticated user.
    """

    return current_user


def require_role(
    role: str,
):
    """
    Require a specific role.
    """

    def role_checker(
    current_user: TokenPayload = Depends(
        get_current_active_user,
    ),
) -> TokenPayload:

        if current_user.role != role:
            raise PermissionDeniedError(
                "You do not have permission to perform this action."
            )

        return current_user

    return role_checker

