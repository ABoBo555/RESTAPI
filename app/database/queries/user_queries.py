"""
SQL queries and stored procedure calls
for user management.
"""

# -----------------------------
# User Management
# -----------------------------

SQL_GET_USERS = """
EXEC dbo.usp_GetUsers
    @Page = ?,
    @PageSize = ?,
    @Search = ?,
    @Role = ?,
    @IsActive = ?;
"""

SQL_GET_USER_BY_ID = """
EXEC dbo.usp_GetUserById
    @UserID = ?;
"""

SQL_CREATE_USER = """
EXEC dbo.usp_CreateUser
    @Username = ?,
    @Email = ?,
    @PasswordHash = ?,
    @Role = ?;
"""

SQL_UPDATE_USER = """
EXEC dbo.usp_UpdateUser
    @UserID = ?,
    @Username = ?,
    @Email = ?,
    @Role = ?,
    @IsActive = ?;
"""

SQL_DELETE_USER = """
EXEC dbo.usp_DeleteUser
    @UserID = ?;
"""

SQL_CHANGE_PASSWORD = """
EXEC dbo.usp_ChangePassword
    @UserID = ?,
    @PasswordHash = ?;
"""