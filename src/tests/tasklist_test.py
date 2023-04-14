import unittest
from entities.tasklist import TaskList


class Test_Tasklist(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()

    def test_adding_task_works(self):
        task_count_at_start = len(self.task_list.tasks)
        self.task_list.add_task("Siivoa huone")
        new_task_count = len(self.task_list.tasks)
        self.assertGreater(new_task_count, task_count_at_start)

    def test_task_removing_works(self):
        task_name = "Heitä roskat"
        self.task_list.add_task(task_name)
        self.assertEqual(len(self.task_list.tasks), 1)
        self.task_list.remove_task(task_name)
        self.assertEqual(len(self.task_list.tasks), 0)
        

    def test_remiving_task_that_don_exist(self):
        task_name = "Heitä roskat"
        self.task_list.add_task(task_name)
        self.task_list.remove_task("Ulkoiluta koira")
        self.assertEqual(len(self.task_list.tasks), 1)