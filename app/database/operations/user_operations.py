import pyodbc

from app.database.operations.db_operations import (
    db_execute_fetch_all,
    db_execute_fetch_one,
    db_execute_insert_update_delete,
    db_execute_scalar,
)

from app.database.queries import *



def db_create_user(
    username: str,
    email: str,
    password_hash: str,
    role: str,
) -> int | None:
    """
    Create a new user.

    Returns:
        Newly created UserID.
    """

    return db_execute_scalar(
        sql=SQL_CREATE_USER,
        params=(
            username,
            email,
            password_hash,
            role,
        ),
    )


def db_get_users(
    page: int,
    page_size: int,
    search: str | None,
    role: str | None,
    is_active: bool | None,
) -> list[pyodbc.Row]:
    """
    Retrieve all users with pagination.
    """

    return db_execute_fetch_all(
        sql=SQL_GET_USERS,
        params=(
            page,
            page_size,
            search,
            role,
            is_active,
        ),
    )


def db_get_user_by_id(
    user_id: int,
) -> pyodbc.Row | None:
    """
    Retrieve a user by ID.
    """

    return db_execute_fetch_one(
        sql=SQL_GET_USER_BY_ID,
        params=(user_id,),
    )


def db_get_user_by_username(
    username: str,
) -> pyodbc.Row | None:
    """
    Retrieve a user by username.
    """

    return db_execute_fetch_one(
        sql=SQL_GET_USER_BY_USERNAME,
        params=(username,),
    )


def db_get_user_by_email(
    email: str,
) -> pyodbc.Row | None:
    """
    Retrieve a user by email.
    """

    return db_execute_fetch_one(
        sql=SQL_GET_USER_BY_EMAIL,
        params=(email,),
    )


def db_update_user(
    user_id: int,
    username: str,
    email: str,
    role: str,
    is_active: bool,
) -> int:
    """
    Update user information.

    Returns:
        Number of affected rows.
    """

    return db_execute_insert_update_delete(
        sql=SQL_UPDATE_USER,
        params=(
            user_id,
            username,
            email,
            role,
            is_active,
        ),
    )


def db_delete_user(
    user_id: int,
) -> int:
    """
    Soft delete a user.

    Returns:
        Number of affected rows.
    """

    return db_execute_insert_update_delete(
        sql=SQL_DELETE_USER,
        params=(user_id,),
    )


def db_change_password(
    user_id: int,
    password_hash: str,
) -> int:
    """
    Change a user's password.

    Returns:
        Number of affected rows.
    """

    return db_execute_insert_update_delete(
        sql=SQL_CHANGE_PASSWORD,
        params=(
            user_id,
            password_hash,
        ),
    )


def db_update_last_login(
    user_id: int,
) -> int:
    """
    Update the user's last login timestamp.

    Returns:
        Number of affected rows.
    """

    return db_execute_insert_update_delete(
        sql=SQL_UPDATE_LAST_LOGIN,
        params=(user_id,),
    )


def db_get_user_credentials(
    user_id: int,
):
    """
    Retrieve authentication credentials for a user.
    """

    return db_execute_fetch_one(
        sql=SQL_GET_USER_CREDENTIALS,
        params=(
            user_id,
        ),
    )