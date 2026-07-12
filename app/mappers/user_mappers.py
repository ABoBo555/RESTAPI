from pyodbc import Row

from app.schemas.user_schemas import (
    UserResponse,
)


def map_user_response(
    row: Row,
) -> UserResponse:
    """
    Map a database row to a UserResponse schema.
    """

    return UserResponse(
        user_id=row.UserID,
        username=row.Username,
        email=row.Email,
        role=row.Role,
        is_active=row.IsActive,
        last_login_at=row.LastLoginAt,
        created_at=row.CreatedAt,
        updated_at=row.UpdatedAt,
    )

