


class TaskDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def add_task(self, task, user_id):
        self.conn.execute(f"INSERT INTO tasks (name, completed, user_id) VALUES (?, ?, ?)", (task.name, int(task.completed), user_id))
        self.conn.commit()

    def update_task(self, task):
        self.conn.execute(f"UPDATE tasks SET name=?, completed=? WHERE id=?", (task.name, int(task.completed), task.id))
        self.conn.commit()

    def delete_task(self, task):
        self.conn.execute(f"DELETE FROM tasks WHERE id=?", (task.id,))
        self.conn.commit()