from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from app.exceptions.employee_exceptions import (
    EmployeeCreationError,
    EmployeeNotFoundError,
)


def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(404)
    async def not_found_handler(
        request: Request,
        exc: HTTPException,
    ):
        return JSONResponse(
            status_code=404,
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
                "detail": str(exc)
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
                "detail": str(exc)
            },
        )