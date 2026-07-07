from fastapi import (
    FastAPI,
    Request,
    status,
)

from fastapi.responses import JSONResponse

from app.exceptions import *

from app.routers import employee_router

from app.schemas import MessageResponse

tags_metadata = [
    {
        "name": "Employees",
        "description": "Employee CRUD Operations",
    },
]


app = FastAPI(
    title="Employee Management API",
    description="REST API built with FastAPI and SQL Server.",
    version="1.0.0",
    contact={
        "name": "Raj Kapoor",
        "email": "robbobroy224@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
    openapi_tags=tags_metadata,
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


app.include_router(employee_router)


@app.get(
    "/",
    response_model=MessageResponse,
    tags=["Root"],
    summary="API Status",
)
def root():

    return MessageResponse(
        message="Employee Management API is running."
    )