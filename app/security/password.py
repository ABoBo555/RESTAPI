from passlib.context import CryptContext


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