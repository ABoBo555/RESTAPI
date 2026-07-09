import pyodbc
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

connection = pyodbc.connect(
                    """
                        DRIVER={ODBC Driver 18 for SQL Server};
                        SERVER=RajKapoor;
                        DATABASE=HR_DB;
                        Trusted_Connection=yes;
                        TrustServerCertificate=yes;
                    """
                )    

cursor = connection.cursor()



# get employee by id ( path parameter)
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):

    cursor.execute(
        """
        SELECT EmployeeID,
               Name,
               Age,
               Department
        FROM Employee
        WHERE EmployeeID = ?
        """,
        (emp_id,)
    )

    row = cursor.fetchone()

    if row is None:
        return {"error": "Employee not found"}

    return {
        "id": row.EmployeeID,
        "name": row.Name,
        "age": row.Age,
        "department": row.Department
    }

# get all employees
@app.get("/employees")
def get_all_employees():

    cursor.execute(
        """
            SELECT * FROM Employee
        """
    )

    rows = cursor.fetchall()

    if rows is None:
        return {"message": "Employee not found"}

    employee_list = []

    for row in rows:

        employee_list.append({
            "id": row.EmployeeID,
            "name": row.Name,
            "age": row.Age,
            "department": row.Department
        })

    return {"employees": employee_list}

# post employee
class Employee(BaseModel):
    name: str
    age: int
    department: str

@app.post("/employees")
def create_employee(employee: Employee):

    cursor.execute(
        """
            INSERT INTO Employee (Name, Age, Department)
            VALUES (?, ?, ?)
        """,
        (employee.name, employee.age, employee.department)
    )

    connection.commit()

    return {"message": "Employee created successfully"}


# put employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, employee: Employee):

    cursor.execute(
        """
            UPDATE Employee
            SET Name = ?, Age = ?, Department = ?
            WHERE EmployeeID = ?
        """,
        (employee.name, employee.age, employee.department, emp_id)
    )

    connection.commit()

    return {"message": "Employee updated successfully"}


@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):

    cursor.execute(
        """
        DELETE
        FROM Employee
        WHERE EmployeeID = ?
        """,
        (emp_id,)
    )

    connection.commit()

    return {
        "message": "Deleted successfully"
    }


