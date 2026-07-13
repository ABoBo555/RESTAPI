from .employee_queries import *
from .user_queries import *
from .authentication_queries import *



__all__ = [
    "GET_ALL_EMPLOYEES",
    "GET_EMPLOYEE_BY_ID",
    "CREATE_EMPLOYEE",
    "UPDATE_EMPLOYEE",
    "DELETE_EMPLOYEE",
    "GET_EMPLOYEE_COUNT",
    "SQL_GET_USERS",
    "SQL_GET_USER_BY_ID",
    "SQL_CREATE_USER",
    "SQL_UPDATE_USER",
    "SQL_DELETE_USER",
    "SQL_CHANGE_PASSWORD",
    "SQL_GET_USER_BY_USERNAME",
    "SQL_GET_USER_BY_EMAIL",
    "SQL_REGISTER_USER",
    "SQL_UPDATE_LAST_LOGIN",
    "SQL_GET_USER_CREDENTIALS",

]