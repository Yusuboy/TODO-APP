import os
import sqlite3
from entities.todoApp import TodoApp


db = sqlite3.connect("TODO.db")
db.isolation_level = None


def create_tables():
    db.execute(
        f"CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT )")
    db.execute(
        f"CREATE TABLE tasks (id INTEGER PRIMARY KEY, todo TEXT, user_id INTEGER REFERENCES Users)")
