from entities.tasks import Task


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        new_task = Task(task)
        self.tasks.append(new_task)

    def remove_task(self, task: str):
        for i in self.tasks:
            if i.name == task:
                self.tasks.remove(i)
