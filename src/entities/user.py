from entities.tasklist import TaskList


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.task_list = TaskList()

    def add_task(self, task):
        self.task_list.add_task(task)

    def remove_task(self, task):
        self.task_list.remove_task(task)
