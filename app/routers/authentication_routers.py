from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.schemas.user_schemas import (
    LoginRequest,
    RegisterUserRequest,
    RegisterUserResponse,
    TokenResponse,
)

from app.services.user_service import (
    register_user,
)

from app.services.authentication_service import (
    login_user,
)


from fastapi.security import (
    OAuth2PasswordRequestForm,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterUserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register User",
)
def register(
    request: RegisterUserRequest,
):
    """
    Register a new user.
    """

    return register_user(request)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Login",
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    Authenticate a user.
    """

    request = LoginRequest(
        login=form_data.username,
        password=form_data.password,
    )

    return login_user(request)