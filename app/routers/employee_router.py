from fastapi import (
    APIRouter,
    Path,
    Response,
    status,
)

from app.services.employee_service import *

from app.schemas import *
from app.exceptions import *

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


@router.get(
    "/",
    response_model=list[EmployeeResponse],
    status_code=status.HTTP_200_OK,
    summary="Get All Employees",
)
def get_employees():
    """
    Retrieve all active employees.
    """

    return get_all_employees()


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Employee By ID",
)
def get_employee(
    employee_id: int = Path(
        ...,
        gt=0,
        description="Employee ID",
    ),
):
    """
    Retrieve an employee by ID.
    """

    return get_employee_by_id(employee_id)


@router.post(
    "/",
    response_model=CreateEmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Employee",
)
def create_new_employee(
    employee: EmployeeCreate,
):
    """
    Create a new employee.
    """

    employee_id = create_employee(employee)

    return CreateEmployeeResponse(
        employee_id=employee_id
    )


@router.put(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Update Employee",
)
def update_existing_employee(
    employee_id: int = Path(
        ...,
        gt=0,
        description="Employee ID",
    ),
    employee: EmployeeUpdate = ...,
):
    """
    Update an existing employee.
    """

    update_employee(
        employee_id,
        employee,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )


@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Employee",
)
def delete_existing_employee(
    employee_id: int = Path(
        ...,
        gt=0,
        description="Employee ID",
    ),
):
    """
    Soft delete an employee.
    """

    delete_employee(employee_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )