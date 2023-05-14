from entities.user import User
from repositories.user_repository import UserDatabase

from database_connection import get_database_connection

class CredentialsBeingIncorrect(Exception):
    pass


class UsernameTakenError(Exception):
    pass


class InvalidUsername(Exception):
    pass

class UserService:

    """
    A class representing a todo application (user).

    Methods:
    __init__(self):
        Initializes a new UserService instance.

    create_user(self, username: str, password: str, signin: bool = True):
        Creates a new user with the given username and password.

    signin(self, username: str, password: str):
        Signs in the user with the given username and password.

    logout(self) :
        Logs out the current user.

    get_current_user(self):
        Gets the current user.

    add_task_to_user(self, user_name: str, task: str):
        Adds a task to the user's task list.

    get_users_tasks(self, user_name: str):
        Gets the tasks of the user with the given username.

    get_users_undone_tasks(self, name: str):
        Gets the undone tasks of the user with the given username.

    get_users_done_tasks(self, name: str):
        Gets the done tasks of the user with the given username.

    remove_task_from_user(self, user_name: str, task: str):
        Removes a task from the user's task list.

    change_user_task_status(self, username: str, task: str):
        Changes the status of a task for the user with the given username.
    """
    def __init__(self):
        """Initializes a new UserService instance."""
        self.user = None
        self.user_db = UserDatabase(get_database_connection())

    def create_user(self, username: str, password: str, signin: True):
        """Creates a new user with the given username and password.

        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            signin (bool, optional): Whether to sign in the new user. Defaults to True.

        Returns:
            User: The newly created user.
        
        Raises:
            UsernameTakenError: If the given username already exists.
        """
        if self.user_db.find_by_username(username):
            raise UsernameTakenError(f"Username {username} already exists")

        if len(username) < 4:
            raise InvalidUsername("Username must be minimum of 4 characters")

        user = User(username, password)
        self.user_db.create_user(user)
        if signin:
            self.user = user

        return user



    def signin(self, username, password):
        """Signs in the user with the given username and password.

        Args:
            username (str): The username of the user to sign in.
            password (str): The password of the user to sign in.
        
        Raises:
            CredentialsBeingIncorrect: If the given username or password is incorrect.
        """
        user = self.user_db.find_by_username(username)
        if user and user[2] == password:
            self.user = User(user[1], user[2])
            return user

        raise CredentialsBeingIncorrect("Invalid username or password")



    def logout(self):
        """Logs out the current user."""
        self.user = None

    def get_current_user(self):
        """Get the currently logged in user.

        Returns:
        User: The currently logged in user.

        """
        return self.user

user_service = UserService()
