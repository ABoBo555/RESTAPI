from pyodbc import Row

from .db_operations import *

from ..queries import *

from app.schemas import *


def db_get_all_employees(
    query: EmployeeListQuery,
) -> list[Row]:
    """
    Retrieve employees from the database.
    """

    return db_execute_fetch_all(
        sql=GET_ALL_EMPLOYEES,
        params=(
            query.page,
            query.page_size,
            query.search,
            query.department,
            query.sort_by.value,
            query.sort_direction.value,
        ),
    )


def db_get_employee_by_id(
    employee_id: int,
) -> Row | None:
    """
    Retrieve an employee by ID.
    """

    return db_execute_fetch_one(
        sql=GET_EMPLOYEE_BY_ID,
        params=(employee_id,),
    )


def db_create_employee(
    employee: EmployeeCreate,
) -> int | None:
    """
    Create a new employee.

    Returns:
        Newly created employee ID.
    """

    return db_execute_scalar(
        sql=CREATE_EMPLOYEE,
        params=(
            employee.name,
            employee.age,
            employee.department,
        ),
    )


def db_update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
) -> int:
    """
    Update an employee.

    Returns:
        Number of affected rows.
    """

    return db_execute_insert_update_delete(
        sql=UPDATE_EMPLOYEE,
        params=(
            employee_id,
            employee.name,
            employee.age,
            employee.department,
        ),
    )


def db_delete_employee(
    employee_id: int,
) -> int:
    """
    Soft delete an employee.

    Returns:
        Number of affected rows.
    """

    return db_execute_insert_update_delete(
        sql=DELETE_EMPLOYEE,
        params=(employee_id,),
    )


def db_get_employee_count(
    query: EmployeeListQuery,
) -> int:
    """
    Retrieve the total number of employees
    matching the query.
    """

    count = db_execute_scalar(
        sql=GET_EMPLOYEE_COUNT,
        params=(
            query.search,
            query.department,
        ),
    )

    return int(count or 0)