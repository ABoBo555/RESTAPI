import pyodbc

from app.mappers import map_employee

from app.database import *

from app.schemas import *
from app.exceptions import *


def get_all_employees() -> list[EmployeeResponse]:
    """
    Retrieve all active employees.
    """

    rows = execute_fetch_all(
        sql="EXEC dbo.usp_GetEmployees"
    )

    return [map_employee(row) for row in rows]


def get_employee_by_id(
    employee_id: int,
) -> EmployeeResponse:
    """
    Retrieve an employee by ID.

    Raises:
        EmployeeNotFoundError:
            If the employee does not exist.
    """

    row = execute_fetch_one(
        sql="""
        EXEC dbo.usp_GetEmployeeById
            @EmployeeID=?
        """,
        params=(employee_id,),
    )

    if row is None:
        raise EmployeeNotFoundError(
            f"Employee with ID {employee_id} was not found."
        )

    return map_employee(row)


def create_employee(
    employee: EmployeeCreate,
) -> int:
    """
    Create a new employee.

    Returns:
        int: Newly created Employee ID.

    Raises:
        EmployeeCreationError:
            If the employee could not be created.
    """

    employee_id = execute_scalar(
        sql="""
        EXEC dbo.usp_CreateEmployee
            @Name=?,
            @Age=?,
            @Department=?
        """,
        params=(
            employee.name,
            employee.age,
            employee.department,
        ),
    )

    if employee_id is None:
        raise EmployeeCreationError(
            "Failed to create employee."
        )

    return int(employee_id)


def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
) -> None:
    """
    Update an existing employee.

    Raises:
        EmployeeNotFoundError:
            If the employee does not exist.
    """

    affected_rows = execute_insert_update_delete(
        sql="""
        EXEC dbo.usp_UpdateEmployee
            @EmployeeID=?,
            @Name=?,
            @Age=?,
            @Department=?
        """,
        params=(
            employee_id,
            employee.name,
            employee.age,
            employee.department,
        ),
    )

    if affected_rows == 0:
        raise EmployeeNotFoundError(
            f"Employee with ID {employee_id} was not found."
        )


def delete_employee(
    employee_id: int,
) -> None:
    """
    Soft delete an employee.

    Raises:
        EmployeeNotFoundError:
            If the employee does not exist.
    """

    affected_rows = execute_insert_update_delete(
        sql="""
        EXEC dbo.usp_DeleteEmployee
            @EmployeeID=?
        """,
        params=(employee_id,),
    )

    if affected_rows == 0:
        raise EmployeeNotFoundError(
            f"Employee with ID {employee_id} was not found."
        )