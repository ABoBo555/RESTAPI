from app.database.operations.db_operations import (
    db_execute_fetch_all,
    db_execute_fetch_one,
    db_execute_insert_update_delete,
    db_execute_scalar,
)


from app.database.queries.user_queries import (
    SQL_GET_USER_BY_EMAIL,
    SQL_GET_USER_BY_USERNAME,
    SQL_REGISTER_USER,
    SQL_UPDATE_LAST_LOGIN,
)

import pyodbc



def db_register_user(
    username: str,
    email: str,
    password_hash: str,
    role: str,
) -> int | None:
    """
    Register a new user.

    Returns:
        Newly created User ID.
    """

    return db_execute_scalar(
        sql=SQL_REGISTER_USER,
        params=(
            username,
            email,
            password_hash,
            role,
        ),
    )


def db_get_user_by_username(
    username: str,
)-> pyodbc.Row | None:
    """
    Retrieve a user by username.
    """

    return db_execute_fetch_one(
        sql=SQL_GET_USER_BY_USERNAME,
        params=(username,),
    )


def db_get_user_by_email(
    email: str,
)-> pyodbc.Row | None:
    """
    Retrieve a user by email.
    """

    return db_execute_fetch_one(
        sql=SQL_GET_USER_BY_EMAIL,
        params=(email,),
    )


def db_update_last_login(
    user_id: int,
) -> int:
    """
    Update user's last login timestamp.
    """

    return db_execute_insert_update_delete(
        sql=SQL_UPDATE_LAST_LOGIN,
        params=(user_id,),
    )

