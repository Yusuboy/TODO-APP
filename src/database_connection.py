import sqlite3
import os

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "data", "TODO.db"))


def get_database_connection():
    return connection