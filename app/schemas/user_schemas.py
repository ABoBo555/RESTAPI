from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)

from app.config import (
    DEFAULT_PAGE_SIZE,
    MAX_PAGE_SIZE,
)


from enum import Enum

class RegisterUserRequest(BaseModel):
    """
    Request model for user registration.
    """

    username: str = Field(
        min_length=3,
        max_length=50,
        description="Unique username.",
    )

    email: EmailStr = Field(
        description="User email address.",
    )

    password: str = Field(
        min_length=8,
        max_length=128,
        description="Plain-text password.",
    )


class LoginRequest(BaseModel):
    """
    Request model for user login.
    """

    login: str = Field(
        min_length=3,
        max_length=255,
        description="Username or email address.",
    )

    password: str = Field(
        min_length=8,
        max_length=128,
        description="User password.",
    )


class RefreshTokenRequest(BaseModel):
    """
    Request model for refreshing an access token.
    """

    refresh_token: str

class UserRole(str, Enum):

    EMPLOYEE = "Employee"

    MANAGER = "Manager"

    HR = "HR"

    ADMIN = "Admin"

    AUDITOR = "Auditor"



class UserDetail(BaseModel):
    """
    Response model returned after retrieving a user.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )

    id: int = Field(
        alias="user_id",
    )

    username: str

    email: EmailStr

    role: UserRole

    is_active: bool

    last_login_at: datetime | None

    created_at: datetime

    updated_at: datetime | None

class UserInformation(BaseModel):
    """
    Lightweight user information for list responses.
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )

    id: int = Field(alias="user_id")

    username: str

    email: EmailStr

    role: UserRole

    is_active: bool


class RegisterUserResponse(BaseModel):
    """
    Response model returned after successful registration.
    """

    message: str

    user: UserDetail


class TokenResponse(BaseModel):
    """
    Response model returned after successful authentication.
    """

    access_token: str

    refresh_token: str

    token_type: str = "bearer"

    expires_in: int

class TokenPayload(BaseModel):
    """
    JWT payload extracted from an access token.
    """

    sub: str

    user_id: int

    role: str

    exp: int



class CreateUserRequest(BaseModel):
    """
    Request model for administrators creating users.
    """

    username: str = Field(
        min_length=3,
        max_length=50,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )

    role: UserRole


class UserListResponse(BaseModel):
    """
    Paginated list of users.
    """

    total_records: int

    page: int

    page_size: int

    users: list[UserInformation]


class UserUpdate(BaseModel):
    """
    Request model for updating users.
    """

    username: str

    email: EmailStr

    role: UserRole

    is_active: bool


class UserListQuery(BaseModel):

    page: int = Field(default=1, ge=1)

    page_size: int = Field(default=DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE)

    search: str | None = None

    role: UserRole | None = None

    is_active: bool | None = None