class InvalidPageError(Exception):
    """
    Raised when the requested page exceeds
    the available number of pages.
    """
    pass


class AuthenticationError(Exception):
    """
    Raised when user authentication fails.
    """
    pass


class UserAlreadyExistsError(Exception):
    """
    Raised when a username or email already exists.
    """
    pass


class InvalidTokenError(Exception):
    """
    Raised when a JWT token is invalid or expired.
    """
    pass


class PermissionDeniedError(Exception):
    """
    Raised when the authenticated user does not have
    permission to perform the requested operation.
    """
    pass

class UserNotFoundError(Exception):
    """
    Raised when the requested user does not exist.
    """
    pass