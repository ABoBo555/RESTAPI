from app.config import (
    EMPLOYEE_ROLE,
)

from app.database.operations.user_operations import (
    db_create_user,
    db_delete_user,
    db_get_user_by_email,
    db_get_user_by_id,
    db_get_user_by_username,
    db_get_users,
    db_update_user,
)

from app.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)

from app.mappers import *

from app.schemas.user_schemas import (
    CreateUserRequest,
    RegisterUserRequest,
    RegisterUserResponse,
    UserDetail,
    UserListQuery,
    UserListResponse,
    UserUpdate,
)

from app.security import (
    hash_password,
)


# ==========================================================
# Private Helper
# ==========================================================

def _validate_unique_user(
    username: str,
    email: str,
) -> None:
    """
    Validate that the username and email
    are unique.
    """

    if db_get_user_by_username(username):
        raise UserAlreadyExistsError(
            f"Username '{username}' already exists."
        )

    if db_get_user_by_email(email):
        raise UserAlreadyExistsError(
            f"Email '{email}' already exists."
        )

def _create_user(
    username: str,
    email: str,
    password: str,
    role: str,
) -> UserDetail:
    """
    Creates a new user.

    Shared by:
        - Public Registration
        - Admin Create User
    """

    _validate_unique_user(
        username=username,
        email=email,
    )

    password_hash = hash_password(password)

    user_id = db_create_user(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role,
    )

    row = db_get_user_by_id(user_id)

    if row is None:
        raise UserNotFoundError(
            "Failed to retrieve newly created user."
        )

    return map_user(row)



def _get_existing_user(
    user_id: int,
):
    """
    Retrieve an existing user.

    Raises:
        UserNotFoundError
            If the user does not exist.
    """

    row = db_get_user_by_id(user_id)

    if row is None:
        raise UserNotFoundError(
            f"User ID {user_id} not found."
        )

    return row


def _ensure_rows_affected(
    affected: int,
    user_id: int,
) -> None:
    """
    Ensure a database operation affected
    at least one row.
    """

    if affected == 0:
        raise UserNotFoundError(
            f"User ID {user_id} not found."
        )


# ==========================================================
# Public Registration
# ==========================================================

def register_user(
    request: RegisterUserRequest,
) -> RegisterUserResponse:
    """
    Register a new public user.

    Every registered user receives
    the Employee role.
    """

    user = _create_user(
        username=request.username,
        email=request.email,
        password=request.password,
        role=EMPLOYEE_ROLE,
    )

    return RegisterUserResponse(
        message="User registered successfully.",
        user=user,
    )


# ==========================================================
# Admin Create User
# ==========================================================

def admin_create_user(
    request: CreateUserRequest,
) -> UserDetail:
    """
    Create a user with any role.

    Admin only.
    """

    return _create_user(
        username=request.username,
        email=request.email,
        password=request.password,
        role=request.role.value,
    )


# ==========================================================
# Get All Users
# ==========================================================

def get_users(
    query: UserListQuery,
) -> UserListResponse:
    """
    Retrieve users.
    """

    rows = db_get_users(
        page=query.page,
        page_size=query.page_size,
        search=query.search,
        role=query.role.value if query.role else None,
        is_active=query.is_active,
    )

    users = map_user_list(rows)

    return UserListResponse(
        total_records=len(users),
        page=query.page,
        page_size=query.page_size,
        users=users,
    )


# ==========================================================
# Get User By ID
# ==========================================================

def get_user_by_id(
    user_id: int,
) -> UserDetail:
    """
    Retrieve a user by ID.
    """

    row = _get_existing_user(user_id)

    return map_user(row)


# ==========================================================
# Update User
# ==========================================================

def update_user(
    user_id: int,
    request: UserUpdate,
) -> None:
    """
    Update user information.
    """

    _get_existing_user(user_id)

    affected = db_update_user(
        user_id=user_id,
        username=request.username,
        email=request.email,
        role=request.role.value,
        is_active=request.is_active,
    )

    _ensure_rows_affected(
        affected,
        user_id,
    )
# ==========================================================
# Delete User
# ==========================================================

def delete_user(
    user_id: int,
) -> None:
    """
    Soft delete a user.
    """

    _get_existing_user(user_id)

    affected = db_delete_user(user_id)

    affected = db_update_user(...)

    _ensure_rows_affected(
        affected,
        user_id,
    )