from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


print("Application starting...")

employee_list = [
    {
     "id": 1,
     "name": "John Doe",
     "age": 30,
     "department": "HR"
    },
    {
     "id": 2,
     "name": "Jane Smith",
     "age": 25,
     "department": "Finance"
    }
]

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    age: int
    department: str

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    department: Optional[str] = None


#get all employees 
@app.get("/employees")
def get_employees():
    print("get_employees fun is executing...")
    return employee_list

#get employee by id ( path parameter)
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):

    for employee in employee_list:

        if employee["id"] == emp_id:
            return employee

    return {
        "message": "Employee not found"
    }


@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, employee: Employee):
    print("update_employee fun is executing...")

    for emp in employee_list:
        if emp["id"] == emp_id:
            emp["name"] = employee.name
            emp["age"] = employee.age
            emp["department"] = employee.department
            return emp

    return {"error": "Employee not found"}

@app.post("/employees")
def create_employee(employee: Employee):
    print("create_employee fun is executing...")

    temp_emp = {
        "id": len(employee_list) + 1,
        "name": employee.name,
        "age": employee.age,
        "department": employee.department
    }

    employee_list.append(temp_emp)
    return employee


@app.patch("/employees/{emp_id}")
def update_employee_partial(emp_id: int, employee: EmployeeUpdate):
    print("update_employee_partial fun is executing...")

    for emp in employee_list:
        if emp["id"] == emp_id:
            if employee.name is not None:
                emp["name"] = employee.name
            if employee.age is not None:
                emp["age"] = employee.age
            if employee.department is not None:
                emp["department"] = employee.department
            return emp

    return {"error": "Employee not found"}


@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    print("delete_employee fun is executing...")

    for emp in employee_list:
        if emp["id"] == emp_id:
            employee_list.remove(emp)
            return {"message": "Employee deleted successfully"}

    return {"error": "Employee not found"}


print("Application loaded")