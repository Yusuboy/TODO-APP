from repositories.task_repository import TaskDatabase
from repositories.user_repository import UserDatabase
from database_connection import get_database_connection





class TodoService:
    """
    A service class that provides methods to manage to-do tasks for users.
    
    Attributes:
        user (str): The username of the current user. Defaults to None.
        task_db (TaskDatabase): A TaskDatabase instance to handle database operations for tasks.
        user_db (UserDatabase): A UserDatabase instance to handle database operations for users.
    """
    def __init__(self):
        """Initializes a new TodoService instance."""
        self.user = None
        self.task_db = TaskDatabase(get_database_connection())
        self.user_db = UserDatabase(get_database_connection())

    def add_task_to_user(self, user_name: str, todo_object: object):
        """Adds a task to a user's list of tasks.

        Args:
            user_name (str): The username of the user whose list the task is being added to.
            todo_object (object): The task being added to the user's list.

        Returns:
            None
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
        return None


    def get_users_undone_tasks(self, name):
        """Returns a list of undone tasks for the specified user.

        Args:
            name (str): The username of the user whose undone tasks are to be returned.

        Returns:
             A list of undone tasks for the specified user or None if the user does not exist.

        """
        user = self.user_db.find_by_username(name)
        if user:
            return self.task_db.get_undone_tasks(name)
        return None



    def get_users_done_tasks(self, name):
        """
        Retrieves a list of all the completed tasks for the given user.

        Args:
            name (str): The name of the user.

        Returns:
            A List of done tasks for the specified user or None if the user does not exist.
        """
        user = self.user_db.find_by_username(name)
        if user:
            return self.task_db.get_done_tasks(name)
        return None


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
        """
        Changes the priority of a task for a given user.

        Args:
            username (str): The username of the user whose task is being modified.
            task (str): The name of the task to modify.
            priority (str): The new priority of the task.

        Returns:
            User object: The user object corresponding to the modified task, if the user is found.
            None
        """
        user = self.user_db.find_by_username(username)
        if user:
            self.task_db.update_users_task_priority(username, task, priority)
            return user
        return None


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
