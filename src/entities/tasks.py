class Task:
    """A class representing a task to be completed.

    Attributes:
        name (str): The name of the task.
        completed (bool): Whether or not the task has been completed.
        priority (str): priority of the task.

    Methods:
        __init__(self, name: str, priority: str = 'low' ): Initializes a new Task instance with the given name and sets task priority low by default.
    """

    def __init__(self, name: str, priority: str = "low"):
        """Initializes a new Task instance with the given name.

        Args:
            name (str): The name of the task.
            priority(str): The priority of the task
        """
        self.priority = 'low'
        self.name = name
        self.priority = priority.lower()
        self.completed = False

        if self.priority not in ['low', 'medium', 'high']:
            raise ValueError("Invalid priority. Valid priorities are 'low', 'medium' or 'high'.")
        
        
        