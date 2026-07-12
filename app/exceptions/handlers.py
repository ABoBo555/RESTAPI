from fastapi import (
    FastAPI,
    Request,
    status,
)
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from .employee_exceptions import (
    EmployeeError,
    EmployeeCreationError,
    EmployeeNotFoundError,
)
from .custom_exceptions import (
    InvalidPageError,
    AuthenticationError,
    UserAlreadyExistsError,
    InvalidTokenError,
    PermissionDeniedError,
    UserNotFoundError,
)



def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all global exception handlers.
    """

    @app.exception_handler(404)
    async def not_found_handler(
        request: Request,
        exc: HTTPException,
    ):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": "The requested endpoint does not exist."
            },
        )

    @app.exception_handler(EmployeeNotFoundError)
    async def employee_not_found_handler(
        request: Request,
        exc: EmployeeNotFoundError,
    ):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(EmployeeCreationError)
    async def employee_creation_handler(
        request: Request,
        exc: EmployeeCreationError,
    ):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(InvalidPageError)
    async def invalid_page_handler(
        request: Request,
        exc: InvalidPageError,
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "detail": str(exc),
            },
        )
    

    @app.exception_handler(AuthenticationError)
    async def authentication_error_handler(
        request: Request,
        exc: AuthenticationError,
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "detail": str(exc),
            },
        )


    @app.exception_handler(UserAlreadyExistsError)
    async def user_already_exists_handler(
        request: Request,
        exc: UserAlreadyExistsError,
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "detail": str(exc),
            },
        )
    

    @app.exception_handler(InvalidTokenError)
    async def invalid_token_handler(
        request: Request,
        exc: InvalidTokenError,
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "detail": str(exc),
            },
            headers={
                "WWW-Authenticate": "Bearer",
            },
        )


    @app.exception_handler(PermissionDeniedError)
    async def permission_denied_handler(
        request: Request,
        exc: PermissionDeniedError,
    ):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(UserNotFoundError)
    async def employee_not_found_handler(
        request: Request,
        exc: UserNotFoundError,
    ):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "detail": str(exc),
            },
        )