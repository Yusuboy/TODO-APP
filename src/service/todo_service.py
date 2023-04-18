from entities.tasks import Task
from entities.user import User
from repositories.user_repository import UserDatabase
from repositories.task_repository import TaskDatabase

from database_connection import get_database_connection


class TodoApp:
    def __init__(self):
        self.users = []
        self.user_db = UserDatabase(get_database_connection())
        self.task_db = TaskDatabase(get_database_connection())
    def create_user(self, name: str, password: str):
        user = User(name, password)
        if user.name not in self.users:

            self.users.append(user)
            self.user_db.create_user(user)

            return user

    def get_user_by_username(self, name: str):
        for user in self.users:
            if user.name == name:
                self.user_db.find_by_username(name)

                return user
        return None

    def add_task_to_user(self, user_name: str, task: str):
        user = self.get_user_by_username(user_name)
        if user:
            user.add_task(task)
            self.task_db.add_task(task, user_name)
            return task
        return None

    def get_users_tasks(self, user_name: str):
        user = self.get_user_by_username(user_name)
        if user:
            self.user_db.get_tasks_of_user(user_name)
            return user.task_list.tasks
        return None

    def get_users_undone_tasks(self, name):
        user = self.get_user_by_username(name)
        if user:
            undone_tasks = []
            for task in user.task_list.tasks:
                if not task.completed:
                    undone_tasks.append(task.name)
                    self.user_db.get_undone_tasks(name)
            return undone_tasks
        return None

    def get_users_done_tasks(self, name):
        user = self.get_user_by_username(name)
        if user:
            done_tasks = []
            for task in user.task_list.tasks:
                if task.completed:
                    done_tasks.append(task.name)
                    self.user_db.get_done_tasks(name)
            return done_tasks
        return None

    def remove_task_from_user(self, user_name: str, task: str):
        user = self.get_user_by_username(user_name)
        if user:
            for i in user.task_list.tasks:
                if i.name == task:
                    user.remove_task(task)
                    self.user_db.delete_task(user_name,task)

    def change_user_task_status(self, username: str, task: str):
        user = self.get_user_by_username(username)
        if user:
            for i in user.task_list.tasks:
                if i.name == task:
                    i.set_completed()
                    self.user_db.update_users_task(username, task)