import unittest
from entities.user import User


class Test_User(unittest.TestCase):
    def setUp(self):
        self.user_test = User('Yusuf', "SQLLover123")

    def test_name_exists(self):
        self.assertNotEqual(self.user_test.name, None)

    def test_name_is_right(self):
        self.assertEqual(self.user_test.name, 'Yusuf')

    def test_password_exists(self):
        self.assertNotEqual(self.user_test.password, None)

    def test_password_is_right(self):
        self.assertEqual(self.user_test.password, 'SQLLover123')

    def test_task_adding_works(self):
        task_count_at_start = len(self.user_test.task_list.tasks)
        task_name = "Käy kaupassa"
        self.user_test.add_task(task_name)
        new_task_count = len(self.user_test.task_list.tasks)
        self.assertGreater(new_task_count, task_count_at_start)

    def test_removing_task_works(self):
        task_name = "Petaa sänky"
        self.user_test.add_task(task_name)
        self.assertEqual(len(self.user_test.task_list.tasks), 1)
        self.user_test.remove_task(task_name)
        self.assertEqual(len(self.user_test.task_list.tasks), 0)
