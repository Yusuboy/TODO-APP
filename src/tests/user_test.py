import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('Yuusuf', 'SQLlover')
    # Test that shows if object exists
    def test_user_exists(self):
        self.assertNotEqual(self.user, None)
    # test that shows username is correct    
    def test_username_is_right(self):
        self.assertEqual(self.user.username, 'Yuusuf')

    # test that shows password is correct    
    def test_password_is_right(self):
        self.assertEqual(self.user.password, 'SQLlover')

    
    