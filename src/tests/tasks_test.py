import unittest
from entities.tasks import Task


class Test_task(unittest.TestCase):
    def setUp(self):
        self.task = Task('Tiskaa')

    def test_task_exists(self):
        self.assertNotEqual(self.task, None)

    def test_task_name_is_right(self):
        self.assertEqual(self.task.name, 'Tiskaa')

    def test_task_priority(self):
        self.assertEqual(self.task.priority, 'low')

        task_high = Task('Task high', 'high')
        self.assertEqual(task_high.priority, 'high')

        task_medium = Task('Task medium', 'medium')
        self.assertEqual(task_medium.priority, 'medium')

     
        with self.assertRaises(ValueError):
            task_invalid = Task('Task invalid', 'invalid')
