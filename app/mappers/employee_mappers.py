import pyodbc

from app.schemas import *

def map_employee_detail(
    row: pyodbc.Row,
) -> EmployeeDetail:
    """
    Convert a database row into an EmployeeDetail model.
    """

    return EmployeeDetail(
        id=row.EmployeeID,
        name=row.Name,
        age=row.Age,
        department=row.Department,
        createdat=row.CreatedAt,
        updatedat=row.UpdatedAt,
    )

def map_employee_summary(
    row: pyodbc.Row,
) -> EmployeeSummary:
    """
    Convert a database row into an EmployeeSummary model.
    """

    return EmployeeSummary(
        id=row.EmployeeID,
        name=row.Name,
        age=row.Age,
        department=row.Department
    )