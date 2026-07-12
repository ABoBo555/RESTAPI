from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)


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


class UserResponse(BaseModel):
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

    role: str

    is_active: bool

    last_login_at: datetime | None

    created_at: datetime

    updated_at: datetime | None


class RegisterUserResponse(BaseModel):
    """
    Response model returned after successful registration.
    """

    message: str

    user: UserResponse


class TokenResponse(BaseModel):
    """
    Response model returned after successful authentication.
    """

    access_token: str

    refresh_token: str

    token_type: str = "Bearer"

    expires_in: int

class TokenPayload(BaseModel):
    """
    JWT payload extracted from an access token.
    """

    sub: str

    user_id: int

    role: str

    exp: int