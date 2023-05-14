class Task:
    """A class representing a task to be completed.

    Attributes:
        name (str): The name of the task.
        completed (bool): Whether or not the task has been completed.
        priority (str): priority of the task.

    Methods:
    __init__(self, name: str, priority: str ): Initializes a new Task instance with the given name and sets.
    """

    def __init__(self, name: str, priority: str):
        """Initializes a new Task instance with the given name.

        Args:
            name (str): The name of the task.
            priority(str): The priority of the task
        """

        self.name = name

        if priority in ['low', 'medium', 'high']:
            self.priority = priority
        else:
            self.priority = 'low'

        self.completed = False
