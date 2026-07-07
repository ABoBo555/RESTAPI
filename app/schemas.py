from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class EmployeeBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=18, lt=65)
    department: str = Field(min_length=2, max_length=50)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int
    createdat: datetime
    updatedat: datetime | None = None


class EmployeePatch(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    age: Optional[int] = Field(default=None, gt=18, lt=65)
    department: Optional[str] = Field(default=None, min_length=2, max_length=50)


class CreateEmployeeResponse(BaseModel):
    employee_id: int

class MessageResponse(BaseModel):
    message: str