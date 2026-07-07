import pyodbc

from app.schemas import *

def map_employee(
    row: pyodbc.Row,
) -> EmployeeResponse:
    """
    Convert a database row into an EmployeeResponse model.
    """

    return EmployeeResponse(
        id=row.EmployeeID,
        name=row.Name,
        age=row.Age,
        department=row.Department,
        createdat=row.CreatedAt,
        updatedat=row.UpdatedAt,
    )