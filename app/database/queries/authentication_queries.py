# -----------------------------
# Authentication
# -----------------------------

SQL_GET_USER_BY_USERNAME = """
EXEC dbo.usp_GetUserByUsername
    @Username = ?;
"""

SQL_GET_USER_BY_EMAIL = """
EXEC dbo.usp_GetUserByEmail
    @Email = ?;
"""

SQL_REGISTER_USER = """
EXEC dbo.usp_CreateUser
    @Username = ?,
    @Email = ?,
    @PasswordHash = ?,
    @Role = ?;
"""

SQL_UPDATE_LAST_LOGIN = """
EXEC dbo.usp_UpdateLastLogin
    @UserID = ?;
"""

SQL_GET_USER_CREDENTIALS = """
EXEC dbo.usp_GetUserCredentials
    @UserID=?;
"""