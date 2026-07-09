import pyodbc

from app import config
from app.logging_config import logger


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

    try:
        return pyodbc.connect(connection_string)

    except pyodbc.Error:
        logger.exception("Failed to establish database connection.")
        raise
