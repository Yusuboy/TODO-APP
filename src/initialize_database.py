from database_connection import get_database_connection

def drop_table(collect):
    db_connect = collect.cursor()
    db_connect.execute("DROP TABLE IF EXISTS Users ")
    db_connect.execute("DROP TABLE IF EXISTS Tasks ")
    collect.commit()

def create_tables(collect):

    db_connect = collect.cursor()

    db_connect.execute("CREATE TABLE Users (id integer PRIMARY KEY, name TEXT, password TEXT);")
    db_connect.execute("CREATE TABLE Tasks "
                   "(id INTEGER PRIMARY KEY, "
                   "user_id INTEGER REFERENCES Users, "
                   "task TEXT, "
                   "completed TEXT NOT NULL"
                   "priority ENUM ('Low', 'Medium', 'High') DEFAULT 'Low'");
    collect.commit()

def initialize_database():
    collect = get_database_connection()
    drop_table(collect)
    create_tables(collect)

initialize_database()
    