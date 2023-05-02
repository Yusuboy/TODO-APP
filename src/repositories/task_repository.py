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

    def delete_task(self, name, task):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Tasks WHERE user_id = "
           "(SELECT id FROM Users WHERE name = ?) "
           "AND task = ?;", (name, task))
        self.connection.commit()

    def get_tasks_of_user(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT t.task, t.completed "
           "FROM Users u "
           "JOIN Tasks t ON u.id = t.user_id "
           "WHERE u.name = ?", (name,))

        tasks = cursor.fetchall()
        
        return tasks

    def update_users_task(self, name, task):
        cursor = self.connection.cursor()
        cursor.execute(
    "UPDATE Tasks SET completed = 1 "
    "WHERE user_id = (SELECT id FROM Users WHERE name = ?) AND task = ?",
    (name, task)
)
        self.connection.commit()

    def get_done_tasks(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""
    SELECT task 
    FROM Tasks 
    WHERE user_id = (
        SELECT id 
        FROM Users 
        WHERE name = ?) 
    AND completed = ?
    """, (name, True))
        tasks = [task[0] for task in cursor.fetchall()]
        self.connection.commit()
        return tasks

    def get_undone_tasks(self, name):
        cursor = self.connection.cursor()
        cursor.execute("""
    SELECT task
    FROM Tasks
    WHERE user_id = (
        SELECT id
        FROM Users
        WHERE name = ?
    )
    AND completed = ?
""", (name, False))
        tasks = [task[0] for task in cursor.fetchall()]
        self.connection.commit()
        return tasks

task_repository = TaskDatabase(get_database_connection())
