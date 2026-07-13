from passlib.context import CryptContext

import re

from app.exceptions import (
    InvalidPasswordError,
)



# Password hashing configuration
_password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(
    password: str,
) -> str:
    """
    Hash a plain-text password using bcrypt.

    Args:
        password: Plain-text password.

    Returns:
        Hashed password.
    """

    return _password_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify a plain-text password against a bcrypt hash.

    Args:
        plain_password: Password entered by the user.
        hashed_password: Stored password hash.

    Returns:
        True if the password matches, otherwise False.
    """

    return _password_context.verify(
        plain_password,
        hashed_password,
    )


def validate_password_strength(
    password: str,
) -> None:
    """
    Validate password strength.

    Rules:
        - Minimum 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character
    """

    if len(password) < 8:
        raise InvalidPasswordError(
            "Password must contain at least 8 characters."
        )

    if not re.search(r"[A-Z]", password):
        raise InvalidPasswordError(
            "Password must contain at least one uppercase letter."
        )

    if not re.search(r"[a-z]", password):
        raise InvalidPasswordError(
            "Password must contain at least one lowercase letter."
        )

    if not re.search(r"\d", password):
        raise InvalidPasswordError(
            "Password must contain at least one digit."
        )

    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        raise InvalidPasswordError(
            "Password must contain at least one special character."
        )

    common_passwords = {
        "password",
        "password123",
        "admin123",
        "admin123!",
        "12345678",
        "qwerty123",
        "welcome123",
    }

    if password.lower() in common_passwords:
        raise InvalidPasswordError(
            "Password is too common. Please choose a stronger password."
        )