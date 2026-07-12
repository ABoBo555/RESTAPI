from fastapi import (FastAPI,)

from app.exceptions import *
from app.routers import *
from app.schemas import MessageResponse
from app.config import APP_VERSION, APP_NAME

tags_metadata = [
    {
        "name": "Root",
        "description": "Application status and information.",
    },
    {
        "name": "Employees",
        "description": "Employee management operations.",
    },
]

app = FastAPI(
    title=APP_NAME,
    description="""
RESTful API for managing employee records.

## Features

- Employee CRUD Operations
- SQL Server Stored Procedures
- Layered Architecture
- Global Exception Handling
- Logging

Built with **FastAPI**, **Pydantic**, **PyODBC**, and **Microsoft SQL Server**.
""",
    version=APP_VERSION,
    contact={
        "name": "Raj Kapoor",
        "email": "robbobroy224@gmail.com",
    },
    license_info={
        "name": "MIT License",
    },
    openapi_tags=tags_metadata,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)



register_exception_handlers(app)

app.include_router(employee_router)
app.include_router(authentication_router)
app.include_router(health_router)



@app.get(
    "/",
    response_model=MessageResponse,
    tags=["Root"],
    summary="API Status",
    description="Check whether the Employee Management API is running.",
)
def root():
    """
    Root endpoint.

    Returns the current API status.
    """

    return MessageResponse(
        message=f"Employee Management API v{app.version} is running."
    )


