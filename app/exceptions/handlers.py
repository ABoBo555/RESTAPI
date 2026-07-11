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