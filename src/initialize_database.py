from database_connection import get_database_connection

def drop_table(collect):
    """
    Drops the Users and Tasks tables from the database.
    
    Args:
        collect: a database connection object.

    """
    db_connect = collect.cursor()
    db_connect.execute("DROP TABLE IF EXISTS Users ")
    db_connect.execute("DROP TABLE IF EXISTS Tasks ")
    collect.commit()

def create_tables(collect):
    """
    Creates the Users and Tasks tables in the database.
    
    Args:
        collect: a database connection object.


    """

    db_connect = collect.cursor()
    db_connect.execute("CREATE TABLE Users (id integer PRIMARY KEY, name TEXT, password TEXT);")
    db_connect.execute("CREATE TABLE Tasks "
                   "(id INTEGER PRIMARY KEY, "
                   "user_id INTEGER REFERENCES Users, "
                   "task TEXT, "
                   "priority TEXT NOT NULL DEFAULT 'low', "
                   "completed TEXT NOT NULL);")


    collect.commit()

def initialize_database():
    """
    Initializes the database. Drops all existing tables and then creates new ones.

    """
    collect = get_database_connection()
    drop_table(collect)
    create_tables(collect)

initialize_database()
    