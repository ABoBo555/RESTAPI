from pydantic import (
    EmailStr,
    TypeAdapter,
    ValidationError,
)

from app.database.operations.user_operations import (
    db_get_user_by_email,
    db_get_user_by_username,
    db_update_last_login,
)

from app.exceptions import (
    AuthenticationError,
    UserAlreadyExistsError,
)

from app.logging_config import logger

from app.mappers import (
    map_user_response,
)

from app.schemas.user_schemas import (
    LoginRequest,
    RegisterUserRequest,
    RegisterUserResponse,
    TokenResponse,
)

from app.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)

from app.constants import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ADMIN_ROLE,
    EMPLOYEE_ROLE,
)


_email_validator = TypeAdapter(EmailStr)


def _is_email(value: str) -> bool:
    """
    Return True if the supplied value is a valid email address.
    """

    try:
        _email_validator.validate_python(value)
        return True

    except ValidationError:
        return False



def login_user(
    request: LoginRequest,
) -> TokenResponse:
    """
    Authenticate a user and return JWT tokens.
    """

    login = request.login.strip()

    logger.info(
        "Login attempt for '%s'.",
        login,
    )

    if _is_email(login):
        login = login.lower()

        row = db_get_user_by_email(
            login,
        )

    else:
        row = db_get_user_by_username(
            login,
        )

    if row is None:
        logger.warning(
            "Login failed. User '%s' not found.",
            login,
        )

        raise AuthenticationError(
            "Invalid username/email or password."
        )

    if not verify_password(
        request.password,
        row.PasswordHash,
    ):
        logger.warning(
            "Invalid password for '%s'.",
            login,
        )

        raise AuthenticationError(
            "Invalid username/email or password."
        )

    db_update_last_login(
        row.UserID,
    )

    access_token = create_access_token(
        user_id=row.UserID,
        username=row.Username,
        role=row.Role,
    )

    refresh_token = create_refresh_token(
        user_id=row.UserID,
        username=row.Username,
        role=row.Role,
    )

    logger.info(
        "User '%s' authenticated successfully.",
        row.Username,
    )

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )
