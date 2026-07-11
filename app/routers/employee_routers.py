from fastapi import (
    APIRouter,
    Path,
    status,
    Depends
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
    response_model= EmployeeListResponse,
    status_code=status.HTTP_200_OK,
    summary="Get All Employees",
)
def get_employees(
    query: EmployeeListQuery = Depends(),
):
    """
    Retrieve employees.

    Supports pagination, searching,
    filtering and sorting.
    """

    return get_all_employees(query)


@router.get(
    "/{employee_id}",
    response_model=EmployeeDetail,
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
    response_model=EmployeeCreateResponse,
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

    return EmployeeCreateResponse(
        id=employee_id,
        message="Employee created successfully."
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

    return MessageResponse(
        message="Employee updated successfully."
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

    return MessageResponse(
        message="Employee deleted successfully."
    )