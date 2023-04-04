import os
import sqlite3


db = sqlite3.connect("TODO.db")
db.isolation_level = None



# luodaan tietokanta
def create_tables():
    db.execute(f"CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT )")
    db.execute(f'CREATE TABLE Todos (id INTEGER PRIMARY KEY, todo TEXT, user_id INTEGER REFERENCES Users)')
    