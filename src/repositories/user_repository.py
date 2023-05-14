from database_connection import get_database_connection
from entities.user import User


class UserDatabase:
    """
    A class that manages user information in a SQLite database.

    Attributes:
        connection: The connection to the database.

    Methods:
        create_user(user: User): Inserts a new user record into the database.
      
        find_by_username(name: str): Finds a user in the database by their username.
        

    """
    def __init__(self, connection):
        """
        Initializes a new instance of the UserDatabase class.

        Args:
            connection: The connection to the database.
        """
        self.connection = connection

    def create_user(self, user):

        """
        Inserts a new user record into the database.

        Args:
            user (User): The user to be inserted into the database.

        Returns:
            User: The user that was inserted into the database.
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (name, password) VALUES (?, ?)",
        (user.name, user.password))
        self.connection.commit()
        return user



    def find_by_username(self, name):
        """
        Finds a user in the database by their username.

        Args:
            name (str): The username of the user to be found.

        Returns:
            Union[User, None]: 
            The user that matches the given username, or None if no such user exists.
        """
        cursor = self.connection.cursor()
        cursor.execute("Select * from Users where name = ?", (name,))
        users = cursor.fetchone()
        return users



user_repository = UserDatabase(get_database_connection())
