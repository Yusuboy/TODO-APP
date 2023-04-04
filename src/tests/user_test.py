import unittest
from entities.user import User
from entities.todo import Todo

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

    # test if list that contains todos is the correct size
    def test_list_size_correct(self):
        
        length = len(self.user.todos)
        
        todo1 = Todo("go to store")
        todo2 = Todo("Call mom")      
        self.user.todos.append(todo1)
        self.user.todos.append(todo2)
        self.assertGreater(len(self.user.todos), length) 
    
    # Create a Todo and test that the size of the todo list is 1
    def test_list_size(self):
        
        todo = Todo("Buy groceries")
        self.user.todos.append(todo)
        self.assertEqual(len(self.user.todos), 1)