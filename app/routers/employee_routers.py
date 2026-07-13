from fastapi import (
    APIRouter,
    Depends,
    Path,
    status,
)

from app.constants import *

from app.schemas import (
    EmployeeCreate,
    EmployeeCreateResponse,
    EmployeeDetail,
    EmployeeListQuery,
    EmployeeListResponse,
    EmployeeUpdate,
    MessageResponse,
)

from app.security import (
    get_current_user,
    require_roles,
)

from app.services.employee_service import (
    create_employee,
    delete_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
)



router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
    dependencies=[
        Depends(get_current_user),
    ],
)


@router.get(
    "/",
    response_model=EmployeeListResponse,
    status_code=status.HTTP_200_OK,
    summary="Get All Employees",
)
def get_employees(
    query: EmployeeListQuery = Depends(),
):
    """
    Retrieve employees.

    Supports pagination, searching,
    filtering, and sorting.
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
        message="Employee created successfully.",
    )


@router.put(
    "/{employee_id}",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
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
        message="Employee updated successfully.",
    )


@router.delete(
    "/{employee_id}",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Employee",
    dependencies=[
        Depends(require_roles(
            ADMIN_ROLE,
            MANAGER_ROLE,
        )),
    ],
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

    Requires the Admin role.
    """

    delete_employee(employee_id)

    return MessageResponse(
        message="Employee deleted successfully.",
    )