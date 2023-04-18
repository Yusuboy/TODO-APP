from database_connection import get_database_connection
from entities.user import User


class UserDatabase:
    def __init__(self, connection):
        self.connection = connection

    def create_user(self, user):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (name, password) VALUES (?, ?)", 
        (user.name, user.password))
        self.connection.commit()
        return user

    def find_all(self):
        cursor = self.connection.cursor()
        cursor.execute("Select * from User")
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = User(*row)
            users.append(user)
        self.connection.commit()
        return users

    def find_by_username(self, name):
        cursor = self.connection.cursor()
        cursor.execute("Select * from Users where name = ?", (name,))
        self.connection.commit()


    def delete_task(self, name, task):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Tasks WHERE user_id = "
           "(SELECT id FROM Users WHERE name = ?) "
           "AND task = ?;", (name, task))
        self.connection.commit()

    def get_tasks_of_user(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT t.task, t.completed "
           "FROM Users u "
           "JOIN Tasks t ON u.id = t.user_id "
           "WHERE u.name = ?", (name,))

        tasks = cursor.fetchall()
        self.connection.commit()
        return tasks

    def update_users_task(self, name, task):
        cursor = self.connection.cursor()
        cursor.execute(
    "UPDATE Tasks SET completed = 1 "
    "WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND task = ?",
    (name, task)
)
        self.connection.commit()

    def get_done_tasks(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""
    SELECT task 
    FROM Tasks 
    WHERE user_id = (
        SELECT id 
        FROM Users 
        WHERE name = ?) 
    AND completed = ?
    """, (name, True))
        tasks = [task[0] for task in cursor.fetchall()]
        self.connection.commit()
        return tasks

    def get_undone_tasks(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""
    SELECT task
    FROM Tasks
    WHERE user_id = (
        SELECT id
        FROM Users
        WHERE name = ?
    )
    AND completed = ?
""", (name, False))
        tasks = [task[0] for task in cursor.fetchall()]
        self.connection.commit()
        return tasks

    def delete_everything(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Users")
        self.connection.commit()


user_repository = UserDatabase(get_database_connection())
