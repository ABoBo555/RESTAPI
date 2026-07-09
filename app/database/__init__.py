from .connection import get_connection
from .operations import *
from .queries import *

__all__ = [
    "get_connection",
    "db_execute_fetch_all",
    "db_execute_fetch_one",
    "db_execute_insert_update_delete",
    "db_execute_scalar",
    "db_get_all_employees",
    "db_get_employee_by_id",
    "db_create_employee",
    "db_update_employee",
    "db_delete_employee",    
    "GET_ALL_EMPLOYEES",
    "GET_EMPLOYEE_BY_ID",
    "CREATE_EMPLOYEE",
    "UPDATE_EMPLOYEE",
    "DELETE_EMPLOYEE",
]