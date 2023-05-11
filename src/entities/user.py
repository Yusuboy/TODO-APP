from entities.tasklist import TaskList

class User:
    """A class representing a user.

    Attributes:
        name (str): The user's name.
        password (str): The user's password.
        task_list (TaskList): The user's list of tasks.

    Methods:
        __init__(self, name: str, password: str): 
        Initializes a new User instance with the given name and password.
        create_task_list(self): 
            Creates a new TaskList for the user.
    """

    def __init__(self, name: str, password: str):
        """Initializes a new User instance with the given name and password.

        Args:
            name (str): The user's name.
            password (str): The user's password.
        """
        self.name = name
        self.password = password
        self.task_list = None

    
