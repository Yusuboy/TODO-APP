import unittest
from service.user_service import UserService, UsernameTakenError, CredentialsBeingIncorrect, InvalidUsername
from service.task_service import TodoService, todo_service
from entities.tasks import Task

class Test_user_service(unittest.TestCase):
    def setUp(self):
        self.task = TodoService()
        self.person = UserService()


    def test_create_user(self):
        
        username = "testuser"
        password = "testpassword"
        user = self.person.create_user(username, password, signin=True)
        self.assertEqual(user.name, username)
        self.assertEqual(user.password, password)


        with self.assertRaises(UsernameTakenError):
            self.person.create_user(username, password, signin=True)


        with self.assertRaises(InvalidUsername):
            self.person.create_user("LOL", 'Salasana', signin=True)


    
    def test_signin(self):
        username = "testuser3"
        password = "testpassword3"
        user = self.person.create_user(username, password, signin=True)

        self.person.signin(username, password)
        self.assertEqual(self.person.get_current_user().name, user.name)
        self.assertEqual(self.person.get_current_user().password, user.password)
        with self.assertRaises(CredentialsBeingIncorrect):
            self.person.signin(username, "incorrectpassword")
        
        with self.assertRaises(CredentialsBeingIncorrect):
            self.person.signin("incorrectusername", password)


    def test_logout(self):
        username = "testuser4"
        password = "testpassword4"

        self.person.create_user(username, password, signin=True)
        self.assertIsNotNone(self.person.get_current_user())
        self.person.logout()
        self.assertIsNone(self.person.get_current_user())