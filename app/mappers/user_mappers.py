from pyodbc import Row

import pyodbc

from app.schemas.user_schemas import (
    UserDetail,
    UserInformation,
)


def map_user(
    row: pyodbc.Row,
) -> UserDetail:
    """
    Map a database row to a UserDetail schema.
    """

    return UserDetail(
        id=row.UserID,
        username=row.Username,
        email=row.Email,
        role=row.Role,
        is_active=row.IsActive,
        last_login_at=row.LastLoginAt,
        created_at=row.CreatedAt,
        updated_at=row.UpdatedAt,
    )


def map_user_list(
    rows: list[pyodbc.Row],
) -> list[UserInformation]:
    """
    Map database rows to a list of UserInformation schemas.
    """

    return [
        UserInformation(
            id=row.UserID,
            username=row.Username,
            email=row.Email,
            role=row.Role,
            is_active=row.IsActive,
        )
        for row in rows
    ]


def map_user_response(
    row: Row,
) -> UserDetail:
    """
    Map a database row to a UserResponse schema.
    """

    return UserDetail(
        user_id=row.UserID,
        username=row.Username,
        email=row.Email,
        role=row.Role,
        is_active=row.IsActive,
        last_login_at=row.LastLoginAt,
        created_at=row.CreatedAt,
        updated_at=row.UpdatedAt,
    )

