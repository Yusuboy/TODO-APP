from database_connection import get_database_connection


class UserDatabase:
    def __init__(self, connection):
        
        self.connection = connection

    def create_user(self, user):
        db = self.connection.cursor()
        db.execute("INSERT INTO Users (name, password) VALUES (?, ?)", (user.name, user.password))
        print(db.execute("Select * from Users").fetchall())
        self.connection.commit()
        

user_repository = UserDatabase(
    get_database_connection())