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



    