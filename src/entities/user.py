
class User:
    """A class representing a user.

    Attributes:
        name (str): The user's name.
        password (str): The user's password.

    Methods:
        __init__(self, name: str, password: str): 
        Initializes a new User instance with the given name and password.
    """

    def __init__(self, name: str, password: str):
        """Initializes a new User instance with the given name and password.

        Args:
            name (str): The user's name.
            password (str): The user's password.
        """
        self.name = name
        self.password = password
    

    
