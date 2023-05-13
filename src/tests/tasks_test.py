import unittest
from entities.tasks import Task


class Test_task(unittest.TestCase):
    def setUp(self):
        self.task = Task('Tiskaa', 'low')
        self.task2 = Task('Tiskaa', 'medium-low')

    def test_task_exists(self):
        self.assertNotEqual(self.task, 'low')

    def test_task_name_is_right(self):
        self.assertEqual(self.task.name, 'Tiskaa')

    def test_task_priority(self):
        self.assertEqual(self.task.priority, 'low')

    def test_if_statment_test(self):
      
        self.assertEqual(self.task2.priority, "low")

   