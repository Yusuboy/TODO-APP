from database_connection import get_database_connection
from entities.user import User

class UserDatabase:
    def __init__(self, connection):
        
        self.connection = connection



    def create_user(self, user):
        db = self.connection.cursor()
        db.execute("INSERT INTO Users (name, password) VALUES (?, ?)", (user.name, user.password))
        self.connection.commit()
        return user

    def find_all(self):
        db = self.connection.cursor()
        db.execute("Select * from User" )
        rows = db.fetchall()
        users = []
        for row in rows:
            user = User(*row)
            users.append(user)
        self.connection.commit()
        return users
    
    def find_by_username(self, name):
        db = self.connection.cursor()
        db.execute("Select * from Users where name = ?", (name,)).fetchall()

        self.connection.commit()

    def find_id_by_username(self, name):
        db = self.connection.cursor()
        db.execute("SELECT id FROM Users WHERE name = ?", (name,))
        result = db.fetchone()
        if result:
            user_id = result[0]
            return User(user_id, name, '')  
        else:
            return None 

        self.connection.commit()

    

    def delete_task(self, name, task):
        db = self.connection.cursor()
        db.execute("DELETE FROM Tasks WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND name = ?;", (name, task))
        self.connection.commit()

    def get_tasks_of_user(self, name):
        db = self.connection.cursor()
        db.execute("SELECT t.task, t.completed FROM Users u JOIN Tasks t ON u.id = t.user_id WHERE u.name = ?", (name,))
        tasks = db.fetchall()
        self.connection.commit()
        return tasks

    def update_users_task(self, name, task):
        db = self.connection.cursor()
        db.execute("UPDATE Tasks SET completed = 1 WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND name = ?", (name, task))
        self.connection.commit()

    
    def get_done_tasks(self, name):
        db = self.connection.cursor()
        db.execute("SELECT task FROM Tasks WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND completed = ?", (name, True))
        tasks = [task[0] for task in db.fetchall()]
        self.connection.commit()
        return tasks
    
    def get_undone_tasks(self, name):
        db = self.connection.cursor()
        db.execute("SELECT task FROM Tasks WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND completed = ?", (name, False))
        tasks = [task[0] for task in db.fetchall()]
        self.connection.commit()
        return tasks




    
    def delete_everything(self):
        db = self.connection.cursor()
        db.execute(f"Delete from Users")
        self.connection.commit()






        

user_repository = UserDatabase(get_database_connection())