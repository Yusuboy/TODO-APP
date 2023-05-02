
from entities.user import User
from repositories.user_repository import UserDatabase
from repositories.task_repository import TaskDatabase

from database_connection import get_database_connection

class CredentialsBeingIncorrect(Exception):
    pass


class UsernameTakenError(Exception):
    pass

class TodoApp:
    def __init__(self):
        self.user = None
        self.user_db = UserDatabase(get_database_connection())
        self.task_db = TaskDatabase(get_database_connection())

    def create_user(self, username: str, password: str, signin: True):
        if self.user_db.find_by_username(username):  
                raise UsernameTakenError(f"Username {username} already exists")
        user = User(username, password)
        self.user_db.create_user(user)
        if signin:
            self.user = user

        return user



    # def get_user_by_username(self, name: str):
    #     for user in self.users:
    #         if user.name == name:
    #             self.user_db.find_by_username(name)
    #             return user
    #     return None


    def signin(self, username, password):
        user = self.user_db.find_by_username(username)
        if user and user[2] == password:
            self.user = User(user[1], user[2])
            return user

        raise CredentialsBeingIncorrect("Invalid username or password")



    def logout(self):
        self.user = None

    def get_current_user(self):
        return self.user


    def add_task_to_user(self, user_name: str, task: str):
        user = self.user_db.find_by_username(user_name)
        if user:
            self.task_db.add_task(task, user_name)
    

    def get_users_tasks(self, user_name: str):
        user = self.user_db.find_by_username(user_name)
        if user:
            return self.user_db.get_tasks_of_user(user_name)
        return None

    def get_users_undone_tasks(self, name):
        user = self.user_db.find_by_username(name)
        if user:
            return self.user_db.get_undone_tasks(name)
        return None

    def get_users_done_tasks(self, name):
        user = self.user_db.find_by_username(name)
        if user:
            return self.user_db.get_done_tasks(name)
        return None

    def remove_task_from_user(self, user_name: str, task: str):
        user = self.user_db.find_by_username(user_name)
        if user:
            self.user_db.delete_task(user_name, task)


    def change_user_task_status(self, username: str, task: str):
        user = self.user_db.find_by_username(username)
        if user:
            self.user_db.update_users_task(username, task)


app_service = TodoApp()
