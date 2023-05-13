from repositories.task_repository import TaskDatabase
from database_connection import get_database_connection
from repositories.user_repository import UserDatabase
from entities.tasks import Task




class TodoService:
    """
    A class representing a todo application (user).
    
    Methods:
    __init__(self):
        Initializes a new TodoService instance.

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
        """Initializes a new TodoService instance."""
        self.user = None
        self.task_db = TaskDatabase(get_database_connection())
        self.user_db = UserDatabase(get_database_connection())
        
    def add_task_to_user(self, user_name: str, todo_object: object):
        """Add a task to a user's task list.

        Args:
        user_name (str): The username of the user whose task list the task will be added to.
        task (str): The name of the task to be added.

        """
        user = self.user_db.find_by_username(user_name)
        if user:
            self.task_db.add_task(todo_object, user_name)

    def get_users_tasks(self, user_name: str):
        """
        Get tasks for the specified user.

        Args:
        user_name (str): The name of the user whose tasks to retrieve.

        Returns:
        list: A list of tasks associated with the specified user.

        Note:
        Returns None if the user does not exist in the database.

        """
        user = self.user_db.find_by_username(user_name)
        if user:
            return self.task_db.get_tasks_of_user(user_name)
        

    def get_users_undone_tasks(self, name):
        """Returns a list of undone tasks for the specified user.

        Args:
            name (str): The username of the user whose undone tasks are to be returned.

        Returns:
            [List[str]]: 
                A list of undone tasks for the specified user or None if the user does not exist.

        """
        user = self.user_db.find_by_username(name)
        if user:
            return self.task_db.get_undone_tasks(name)
        

    def get_users_done_tasks(self, name):
        """
        Retrieves a list of all the completed tasks for the given user.

        Args:
            name (str): The name of the user.

        Returns:
            [List[str]]: 
                A List of done tasks for the specified user or None if the user does not exist.
        """
        user = self.user_db.find_by_username(name)
        if user:
            return self.task_db.get_done_tasks(name)
        

    def remove_task_from_user(self, user_name: str, task: str):
        """Removes a task from a user's task list.

        Args:
        user_name (str): The username of the user whose task list is to be modified.
        task (str): The task to be removed from the user's task list.
        """
        user = self.user_db.find_by_username(user_name)
        if user:
            self.task_db.delete_task(user_name, task)


    def change_task_priority(self, username: str, task: str, priority: str):
        user = self.user_db.find_by_username(username)
        if user:
            self.task_db.update_users_task_priority(username, task, priority)
            return user
       


    def change_user_task_status(self, username: str, task: str):
        """Change the status of a task for a user.

        Args:
            username (str): The username of the user.
            task (str): The task to change the status of.

        
        """
        user = self.user_db.find_by_username(username)
        if user:
            self.task_db.update_users_task(username, task)


todo_service = TodoService()