from .employee_queries import *
from .user_queries import *


__all__ = [
    "GET_ALL_EMPLOYEES",
    "GET_EMPLOYEE_BY_ID",
    "CREATE_EMPLOYEE",
    "UPDATE_EMPLOYEE",
    "DELETE_EMPLOYEE",
    "GET_EMPLOYEE_COUNT",
    "SQL_REGISTER_USER",
    "SQL_GET_USER_BY_USERNAME",
    "SQL_GET_USER_BY_EMAIL",
    "SQL_UPDATE_LAST_LOGIN",
]