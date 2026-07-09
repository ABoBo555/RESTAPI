from app.database import *

from app.exceptions import *

from app.logging_config import logger

from app.mappers import *

from app.schemas import *


def get_all_employees(
    query: EmployeeListQuery,
) -> list[EmployeeSummary]:
    """
    Retrieve employees.
    """

    logger.info(
        "Fetching employees (page=%s, page_size=%s).",
        query.page,
        query.page_size,
    )

    rows = db_get_all_employees(query)

    logger.info(
        "Retrieved %s employee(s).",
        len(rows),
    )

    return [
        map_employee_summary(row)
        for row in rows
    ]


def get_employee_by_id(
    employee_id: int,
) -> EmployeeDetail:
    """
    Retrieve an employee by ID.

    Raises:
        EmployeeNotFoundError:
            If the employee does not exist.
    """

    logger.info(
        "Fetching employee with ID %s.",
        employee_id,
    )

    row = db_get_employee_by_id(employee_id)

    if row is None:

        logger.warning(
            "Employee with ID %s was not found.",
            employee_id,
        )

        raise EmployeeNotFoundError(
            f"Employee with ID {employee_id} was not found."
        )

    logger.info(
        "Employee with ID %s retrieved successfully.",
        employee_id,
    )

    return map_employee_detail(row)


def create_employee(
    employee: EmployeeCreate,
) -> int:
    """
    Create a new employee.

    Returns:
        Newly created employee ID.

    Raises:
        EmployeeCreationError:
            If the employee could not be created.
    """

    logger.info(
        "Creating employee '%s'.",
        employee.name,
    )

    employee_id = db_create_employee(employee)

    if employee_id is None:

        logger.error(
            "Failed to create employee '%s'.",
            employee.name,
        )

        raise EmployeeCreationError(
            "Failed to create employee."
        )

    logger.info(
        "Employee '%s' created successfully with ID %s.",
        employee.name,
        employee_id,
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

    logger.info(
        "Updating employee with ID %s.",
        employee_id,
    )

    affected_rows = db_update_employee(
        employee_id,
        employee,
    )

    if affected_rows == 0:

        logger.warning(
            "Employee with ID %s was not found.",
            employee_id,
        )

        raise EmployeeNotFoundError(
            f"Employee with ID {employee_id} was not found."
        )

    logger.info(
        "Employee with ID %s updated successfully.",
        employee_id,
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

    logger.info(
        "Deleting employee with ID %s.",
        employee_id,
    )

    affected_rows = db_delete_employee(
        employee_id,
    )

    if affected_rows == 0:

        logger.warning(
            "Employee with ID %s was not found.",
            employee_id,
        )

        raise EmployeeNotFoundError(
            f"Employee with ID {employee_id} was not found."
        )

    logger.info(
        "Employee with ID %s deleted successfully.",
        employee_id,
    )