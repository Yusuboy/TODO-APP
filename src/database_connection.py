import sqlite3
from config import DATABASE_FILE_PATH




connection = sqlite3.connect(DATABASE_FILE_PATH)
"""Module for handling database connection.

    Returns:
        sqlite3.Connection: a connection object to the database.
    """

def get_database_connection():
    return connection
    