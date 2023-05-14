from database_connection import get_database_connection



class TaskDatabase:
    """
    A class that represents a database of tasks for multiple users.

    Attributes:
        connection: A database connection object.

    Methods:
        add_task(task_object: object, user_name: str):
            Adds a new task to the database for the given user.
        delete_task(name, task):
            Deletes a task from the database for the given user.
        get_tasks_of_user(name):
            Returns a list of all tasks for the given user.
        update_users_task(name, task):
            Marks a task as completed for the given user.
        update_users_task_priority(name, task, priority):
            Updates the priority of a task for the given user.
        get_done_tasks(name):
            Returns a list of all completed tasks for the given user.
        get_undone_tasks(name):
            Returns a list of all incomplete tasks for the given user.
    """
    def __init__(self, connection):
        """
        Initializes the TaskDatabase object.

        Args:
            connection: A database connection object.
        """
        self.connection = connection

    def add_task(self, task_object: object, user_name: str):

        """
        Adds a new task to the database for the given user.

        Args:
            task_object: An object representing the task to be added.
            user_name: The name of the user to whom the task belongs.
        """
        cursor = self.connection.cursor()
        user_id = cursor.execute("SELECT id FROM Users WHERE name = ?", (user_name,)).fetchone()
        user_id = user_id[0]
        task = task_object.name
        priority = task_object.priority

        cursor.execute("INSERT INTO Tasks (user_id, task, priority, completed) VALUES (?, ?, ?, ?)",
        (user_id, task, priority, False))
        self.connection.commit()

    def delete_task(self, name, task):
        """
        Deletes a task from the database for the given user.

        Args:
            name: The name of the user who owns the task.
            task: The name of the task to be deleted.
        """
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Tasks WHERE user_id = "
           "(SELECT id FROM Users WHERE name = ?) "
           "AND task = ?;", (name, task))
        self.connection.commit()

    def get_tasks_of_user(self, name):
        """
        Returns a list of all tasks for the given user.

        Args:
            name: The name of the user whose tasks are to be retrieved.

        Returns:
            A list of tuples representing the tasks for the given user Tuple has name of the task,
            whether it has been completed (as a boolean), and its priority.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT t.task, t.completed, t.priority "
           "FROM Users u "
           "JOIN Tasks t ON u.id = t.user_id "
           "WHERE u.name = ?", (name,))

        tasks = cursor.fetchall()
        return tasks

    def update_users_task(self, name, task):
        """
        Marks a task as completed for the given user.

        Args:
            name: The name of the user who owns the task.
            task: The name of the task to be marked as completed.
        """
        cursor = self.connection.cursor()
        cursor.execute(
    "UPDATE Tasks SET completed = 1 "
    "WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND task = ?",
    (name, task)
)
        self.connection.commit()


    def update_users_task_priority(self, name, task, priority):
        cursor = self.connection.cursor()

        cursor.execute(
    "UPDATE Tasks SET priority = ? "
    "WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND task = ?",
    (priority, name, task)
)
        self.connection.commit()

    def get_done_tasks(self, name):
        """Returns a list of all completed tasks for a given user.

    Args:
        name (str): The name of the user to retrieve tasks for.

    Returns:
        list: A list of strings, each representing a completed task for the user.
    """
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
        """Returns a list of all incomplete tasks for a given user.

    Args:
        name (str): The name of the user to retrieve tasks for.

    Returns:
        list: A list of strings, each representing an incomplete task for the user.
    """
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

task_repository = TaskDatabase(get_database_connection())
