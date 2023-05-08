class Task:
    """A class representing a task to be completed.

    Attributes:
        name (str): The name of the task.
        completed (bool): Whether or not the task has been completed.

    Methods:
        __init__(self, name: str): Initializes a new Task instance with the given name.
    """

    def __init__(self, name: str):
        """Initializes a new Task instance with the given name.

        Args:
            name (str): The name of the task.
        """
        self.name = name
        self.completed = False
        
        
        