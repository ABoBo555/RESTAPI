"""
SQL queries and stored procedure calls
for Authentication/User operations.
"""

# ---------------------------------------------------------
# Register User
# ---------------------------------------------------------

SQL_REGISTER_USER = """
EXEC dbo.usp_RegisterUser
    @Username=?,
    @Email=?,
    @PasswordHash=?,
    @Role=?
"""


# ---------------------------------------------------------
# Get User By Username
# ---------------------------------------------------------

SQL_GET_USER_BY_USERNAME = """
EXEC dbo.usp_GetUserByUsername
    @Username=?
"""


# ---------------------------------------------------------
# Get User By Email
# ---------------------------------------------------------

SQL_GET_USER_BY_EMAIL = """
EXEC dbo.usp_GetUserByEmail
    @Email=?
"""


# ---------------------------------------------------------
# Update Last Login
# ---------------------------------------------------------

SQL_UPDATE_LAST_LOGIN = """
EXEC dbo.usp_UpdateLastLogin
    @UserID=?
"""


