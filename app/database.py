from typing import Any

import pyodbc

from app import config


def get_connection() -> pyodbc.Connection:
    """
    Create and return a new SQL Server database connection.
    """

    connection_string = (
        f"DRIVER={{{config.DB_DRIVER}}};"
        f"SERVER={config.DB_SERVER};"
        f"DATABASE={config.DB_DATABASE};"
        f"Encrypt={config.DB_ENCRYPT};"
        f"TrustServerCertificate={config.DB_TRUST_SERVER_CERTIFICATE};"
    )

    if config.DB_AUTH_MODE.lower() == "windows":
        connection_string += "Trusted_Connection=yes;"
    else:
        connection_string += (
            f"UID={config.DB_USERNAME};"
            f"PWD={config.DB_PASSWORD};"
        )

    return pyodbc.connect(connection_string)


def execute_fetch_all(
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

        finally:
            cursor.close()


def execute_fetch_one(
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

        finally:
            cursor.close()


def execute_insert_update_delete(
    sql: str,
    params: tuple[Any, ...] = (),
) -> int:
    """
    Execute an INSERT, UPDATE or DELETE stored procedure.

    IMPORTANT:
    The stored procedure must return:

        SELECT @@ROWCOUNT AS AffectedRows

    Returns:
        int: Number of affected rows.
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
            raise

        finally:
            cursor.close()


def execute_scalar(
    sql: str,
    params: tuple[Any, ...] = (),
) -> Any:
    """
    Execute a query that returns a single scalar value.

    Examples:
        - SELECT COUNT(*)
        - SELECT SCOPE_IDENTITY()
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
            raise

        finally:
            cursor.close()


__all__ = [
    "get_connection",
    "execute_fetch_all",
    "execute_fetch_one",
    "execute_insert_update_delete",
    "execute_scalar",
]