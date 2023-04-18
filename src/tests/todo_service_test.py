import unittest
from service.todo_service import TodoApp

class Test_todo_service(unittest.TestCase):
    def setUp(self):
        self.todo = TodoApp()

    def test_create_user(self):
        user = self.todo.create_user("Yuusuf", "password")
        self.assertEqual(user.name, "Yuusuf")
        self.assertEqual(user.password, "password")
        self.assertIn(user, self.todo.users)
    
    def test_add_task_to_user(self):
    
        name = "Yuusuf"
        password = "SQLlover"
        task_name = "Siivoa huone"
        user = self.todo.create_user(name, password)

        self.todo.add_task_to_user(name, task_name)
        self.assertIn(task_name, [task.name for task in user.task_list.tasks])

    
    def test_get_users_tasks(self):
        
        user = self.todo.create_user('Test User', 'password')
        self.todo.add_task_to_user(user.name, 'Task 1')
        tasks = self.todo.get_users_tasks(user.name)
        self.assertNotEqual(tasks, None)

   
        self.assertEqual(tasks[0].name, 'Task 1')

    
    def test_get_users_done_tasks(self):
        
        user = self.todo.create_user("Yuusuf", "password")
        self.todo.add_task_to_user("Yuusuf", "Task 1")
        done_tasks = self.todo.get_users_done_tasks("Yuusuf")
        self.assertEqual(len(done_tasks), 0)
       


    def test_get_users_undone_tasks(self):
    
        user = self.todo.create_user("Yuusuf", "password")
        self.todo.add_task_to_user("Yuusuf", "Task 1")
        undone_tasks = self.todo.get_users_undone_tasks("Yuusuf")
        self.assertEqual(len(undone_tasks), 1)
        self.assertEqual(undone_tasks[0], "Task 1")

    
    def test_remove_task_from_user_method(self):
        name = "Yuusuf"
        password = "SQLlover"
        task_name = "Siivoa huone"
        user = self.todo.create_user(name, password)

        self.todo.add_task_to_user(name, task_name)
        self.todo.remove_task_from_user(name, task_name)
        self.assertNotIn(
        task_name, [task.name for task in user.task_list.tasks])


    def test_user_tasks_status_changes(self):
        name = "Yuusuf"
        password = "SQLlover"
        task_name = "Siivoa huone"
        user = self.todo.create_user(name, password)
        self.todo.add_task_to_user(name, task_name)
        
        # Test that the task is initially marked as incomplete
        self.assertEqual(user.task_list.tasks[0].completed, False)
        
        # Mark the task as complete and test that it has changed
        self.todo.change_user_task_status(name, task_name)
        self.assertEqual(user.task_list.tasks[0].completed, True)
        
        
        

