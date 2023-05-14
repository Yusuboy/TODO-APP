import sqlite3
"""Module for handling database connection.

    Returns:
        sqlite3.Connection: a connection object to the database.
    """

from config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)


def get_database_connection():
    return connection
    