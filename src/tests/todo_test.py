import unittest
from entities.todo import Todo

class TestUser(unittest.TestCase):
    def setUp(self):
        self.todo = Todo('Suorita viikko 3 tehtävät')
    
    # Test that shows if todo-text exists
    def test_text_exists(self):
        self.assertNotEqual(self.todo, None)

    # test that shows todo-text is correct   
    def test_text_is_correct(self):
        self.assertEqual(Self.todo.text, 'Suorita viikko 3 tehtävät')

    def test_completed_is_right(self):
        self.assertEqual(self.todo.completed, False)

    