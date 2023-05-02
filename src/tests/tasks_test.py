import unittest
from entities.tasks import Task


class Test_task(unittest.TestCase):
    def setUp(self):
        self.task = Task('Tiskaa')

    def test_task_exists(self):
        self.assertNotEqual(self.task, None)

    def test_task_name_is_right(self):
        self.assertEqual(self.task.name, 'Tiskaa')

