import unittest
from repositories.user_repository import UserDatabase
from entities.user import User
from database_connection import get_database_connection

class Test_UserDatabase(unittest.TestCase):
    def setUp(self):
        connection = get_database_connection()
        self.user_db = UserDatabase(connection)
        self.user = User(name='testuser', password='testpassword')
        self.user = User(name='testuser8', password='testpassword')


    def test_create_user(self):
        created_user = self.user_db.create_user(self.user)
        self.assertEqual(created_user.name, self.user.name)
        self.assertEqual(created_user.password, self.user.password)


    def test_find_by_username(self):
        found_user = self.user_db.find_by_username(self.user.name)
        self.assertEqual(found_user[1], self.user.name)
        self.assertEqual(found_user[2], self.user.password)

    
    
