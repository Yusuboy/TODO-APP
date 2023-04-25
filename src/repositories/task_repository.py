from database_connection import get_database_connection



class TaskDatabase:
    def __init__(self, connection):
        self.connection = connection

    def add_task(self, task_name, user_name):
        cursor = self.connection.cursor()
        user_id = cursor.execute("SELECT id FROM Users WHERE name = ?", (user_name,)).fetchone()
        if user_id:
            user_id = user_id[0]
            cursor.execute("INSERT INTO Tasks (user_id, task, completed) VALUES (?, ?, ?)",
           (user_id, task_name, False))
            self.connection.commit()
task_repository = TaskDatabase(get_database_connection())
