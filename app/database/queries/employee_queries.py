"""
Employee-related SQL Server stored procedure definitions.
"""

GET_ALL_EMPLOYEES = """
EXEC dbo.usp_GetEmployees
    @Page=?,
    @PageSize=?,
    @Search=?,
    @Department=?,
    @SortBy=?,
    @SortDirection=?
"""

GET_EMPLOYEE_BY_ID = """
EXEC dbo.usp_GetEmployeeById
    @EmployeeID=?
"""

CREATE_EMPLOYEE = """
EXEC dbo.usp_CreateEmployee
    @Name=?,
    @Age=?,
    @Department=?
"""

UPDATE_EMPLOYEE = """
EXEC dbo.usp_UpdateEmployee
    @EmployeeID=?,
    @Name=?,
    @Age=?,
    @Department=?
"""

DELETE_EMPLOYEE = """
EXEC dbo.usp_DeleteEmployee
    @EmployeeID=?
"""