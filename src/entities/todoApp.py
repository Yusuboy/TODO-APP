from entities.tasks import Task
from entities.user import User
from repositories.user_repository import UserDatabase

from database_connection import get_database_connection


class TodoApp:
    def __init__(self):
        self.users = []
        self.user_db = UserDatabase(get_database_connection())
        

        

    def create_user(self, name: str, password: str):
        user = User(name, password)
        self.users.append(user)
        self.user_db.create_user(user)

        return user

    def get_user_by_username(self, name: str):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def add_task_to_user(self, user_name: str, task: str):
        user = self.get_user_by_username(user_name)
        if user:
            user.add_task(task)

    def remove_task_from_user(self, user_name: str, task: str):
        user = self.get_user_by_username(user_name)
        if user:
            user.remove_task(task)

    def change_user_task_status(self, username: str, task: str):
        user = self.get_user_by_username(username)
        if user:
            for i in user.task_list.tasks:
                if i.name == task:
                    i.set_completed()
