import unittest
from entities.todoApp import TodoApp

class Test_TodoApp(unittest.TestCase):
    def setUp(self):
        self.todo = TodoApp()
    
    def test_create_user_method(self):
        name = 'Yuusuf'
        password = 'SQLlover'

        user = self.todo.create_user(name, password)
        self.assertIn(user, self.todo.users)
        self.assertEqual(user.name, name)
        self.assertEqual(user.password, password)

    def test_get_user_by_username_method(self):
    # Arrange
        name = 'Yuusuf'
        password = 'SQLlover'
        
        
        user = self.todo.create_user(name, password)
        retrieved_user = self.todo.get_user_by_username(name)
        self.assertEqual(user, retrieved_user)


    def test_get_user_by_username_is_none(self):

        name = 'Yuusuf'
        password = 'SQLlover'
        name2 = 'Pekka'
        password2 = 'SQLhater'
        

        user = self.todo.create_user(name, password)
        retrieved_user = self.todo.get_user_by_username(name2)
        self.assertEqual(retrieved_user, None)

    def test_add_task_to_user_method(self):
        name = "Yuusuf"
        password = "SQLlover"
        task_name = "Siivoa huone"
        user = self.todo.create_user(name, password)

     
        self.todo.add_task_to_user(name, task_name)
        self.assertIn(task_name, [task.name for task in user.task_list.tasks])

    def test_add_task_to_user_method_no_user(self):
        result = self.todo.add_task_to_user("Pekka", 'Imuroi huone')

        self.assertFalse(result)


    def test_remove_task_from_user_method(self):
        name = "Yuusuf"
        password = "SQLlover"
        task_name = "Siivoa huone"
        user = self.todo.create_user(name, password)

     
        self.todo.add_task_to_user(name, task_name)
        self.todo.remove_task_from_user(name, task_name)
        self.assertNotIn(task_name,[task.name for task in user.task_list.tasks])

    def test_remove_task_from_user_method_no_user(self):
        result = self.todo.remove_task_from_user("pekka", 'Imuroi huone')

      
        self.assertFalse(result)


    def test_change_user_task_status_method(self):
     
        name = "Yuusuf"
        password = "SQLlover"
        task_name = "Käy kaupassa"
        user = self.todo.create_user(name, password)
        self.todo.add_task_to_user(name, task_name)

        self.todo.change_user_task_status(name, task_name)


        self.assertTrue(user.task_list.tasks[0].completed)


    def test_change_user_task_status_method_user_false(self):
    
        virhe = self.todo.change_user_task_status("Yonis", 'Imuroi')
         
        self.assertFalse(virhe)

    
    def test_change_user_task_status_method_task_false(self):
        name = "Yuusuf"
        password = "SQLlover"
        task_name = "Käy kaupassa"
        user = self.todo.create_user(name, password)
        self.todo.add_task_to_user(name, 'Harjoittelee tenttiin')
        virhe = self.todo.change_user_task_status(name, 'Imuroi')

        self.assertFalse(virhe)
        
        

