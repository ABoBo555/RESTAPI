from enum import Enum

from pydantic import (
    BaseModel,
    Field,
)

from app.constants import (DEFAULT_PAGE_SIZE,
    MAX_PAGE_SIZE,
)




class EmployeeSortField(str, Enum):
    """
    Supported fields for sorting employees.
    """

    ID = "id"
    NAME = "name"
    AGE = "age"
    DEPARTMENT = "department"
    CREATED_AT = "createdat"
    UPDATED_AT = "updatedat"


class SortDirection(str, Enum):
    """
    Supported sort directions.
    """

    ASC = "asc"
    DESC = "desc"


class EmployeeListQuery(BaseModel):
    """
    Query parameters used when retrieving employees.
    """

    page: int = Field(
        default=1,
        ge=1,
        description="Page number.",
    )

    page_size: int = Field(
        default=DEFAULT_PAGE_SIZE,
        ge=1,
        le=MAX_PAGE_SIZE,
        description="Number of records per page.",
    )

    search: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Search employees by name.",
    )

    department: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
        description="Filter employees by department.",
    )

    sort_by: EmployeeSortField = Field(
        default=EmployeeSortField.ID,
        description="Field used for sorting.",
    )

    sort_direction: SortDirection = Field(
        default=SortDirection.ASC,
        description="Sorting direction.",
    )