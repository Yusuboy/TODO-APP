import sqlite3
import os


if os.path.exists("Todo.db"):
    os.remove("Todo.db")

db = sqlite3.connect("Todo.db")
db.isolation_level = None

def create_table():
    db.execute(f"create table User (id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    db.execute(f"create table todos (id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES User, tasks TEXT, completed INTEGER NOT NULL)")

create_table()
