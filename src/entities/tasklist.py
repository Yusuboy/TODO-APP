from entities.tasks import Task

class TaskList:
    """A class representing a list of tasks.

    Attributes:
        tasks (list): A list of Task objects.

    Methods:
        __init__(self): Initializes a new TaskList instance with an empty list of tasks.
        add_task(self, task: str): Adds a new task to the list of tasks.
        remove_task(self, task: str): Removes a task from the list of tasks by its name.
    """

    def __init__(self):
        """Initializes a new TaskList instance with an empty list of tasks."""
        self.tasks = []

    def add_task(self, task: str):
        """Adds a new task to the list of tasks.

        Args:
            task (str): The name of the task to be added.
        """
        new_task = Task(task)
        self.tasks.append(new_task)

    def remove_task(self, task: str):
        """Removes a task from the list of tasks by its name.

        Args:
            task (str): The name of the task to be removed.
        """
        for i in self.tasks:
            if i.name == task:
                self.tasks.remove(i)
