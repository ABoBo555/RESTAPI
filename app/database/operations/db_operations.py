from typing import Any

from ..connection import get_connection

from app.logging_config import logger

from ..queries import *

from app.schemas import *

import pyodbc


def db_execute_fetch_all(
    sql: str,
    params: tuple[Any, ...] = (),
) -> list[pyodbc.Row]:
    """
    Execute a query and return all rows.
    """

    with get_connection() as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(sql, params)
            return cursor.fetchall()

        except pyodbc.Error:
            logger.exception(
                "Database error executing execute_fetch_all SQL: %s | Params: %s",
                sql,
                params,
            )
            raise

        finally:
            cursor.close()


def db_execute_fetch_one(
    sql: str,
    params: tuple[Any, ...] = (),
) -> pyodbc.Row | None:
    """
    Execute a query and return a single row.
    """

    with get_connection() as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(sql, params)
            return cursor.fetchone()

        except pyodbc.Error:
            logger.exception(
                "Database error executing execute_fetch_one SQL: %s | Params: %s",
                sql,
                params,
            )
            raise

        finally:
            cursor.close()


def db_execute_insert_update_delete(
    sql: str,
    params: tuple[Any, ...] = (),
) -> int:
    """
    Execute an INSERT, UPDATE or DELETE stored procedure.
    """

    with get_connection() as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(sql, params)

            row = cursor.fetchone()

            connection.commit()

            return row.AffectedRows if row else 0

        except pyodbc.Error:
            connection.rollback()

            logger.exception(
                "Database error executing execute_insert_update_delete SQL: %s | Params: %s",
                sql,
                params,
            )

            raise

        finally:
            cursor.close()


def db_execute_scalar(
    sql: str,
    params: tuple[Any, ...] = (),
) -> Any:
    """
    Execute a query that returns a single scalar value.
    """

    with get_connection() as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(sql, params)

            row = cursor.fetchone()

            connection.commit()

            return row[0] if row else None

        except pyodbc.Error:
            connection.rollback()

            logger.exception(
                "Database error executing execute_scalar SQL: %s | Params: %s",
                sql,
                params,
            )

            raise

        finally:
            cursor.close()


