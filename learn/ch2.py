from fastapi import FastAPI
from pydantic import BaseModel

print("Application starting...")
print("FastAPI obj creating...")

app = FastAPI()

class Employee(BaseModel):
    name: str
    age: int
    department: str


@app.post("/employees")
def create_employee(employee: Employee):
    print("create_employee fun is executing...")
    print(employee.name, " ", employee.age, " ", employee.department)
    return employee

print("FastAPI obj created...")