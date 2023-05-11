import unittest
from service.todo_service import TodoApp, UsernameTakenError, CredentialsBeingIncorrect

class Test_todo_service(unittest.TestCase):
    def setUp(self):
        self.todo = TodoApp()


    def test_create_user(self):
        
        username = "testuser"
        password = "testpassword"
        user = self.todo.create_user(username, password, signin=True)
        self.assertEqual(user.name, username)
        self.assertEqual(user.password, password)


        with self.assertRaises(UsernameTakenError):
            self.todo.create_user(username, password, signin=True)

       
    
    def test_add_task_to_user(self):
        self.todo.create_user("Pekka", "password", signin=True)
        self.todo.add_task_to_user('Pekka', "newww")
        Tasks = self.todo.get_users_tasks("Pekka")
        count1 = len(Tasks)
        self.todo.add_task_to_user("Pekka", "Hellou")
        Tasks2 = self.todo.get_users_tasks("Pekka")
        count2 = len(Tasks2)
        self.assertNotEqual(count1, count2)
        self.assertIsNone(self.todo.add_task_to_user("Pekka2", 'task'))

      

    
    def test_get_users_tasks(self):
   
        username = "test_user"
        password = "test_password"
        self.todo.create_user(username, password, signin=True)
        self.todo.add_task_to_user(username, "task1")
        self.todo.add_task_to_user(username, "task2")
        self.todo.add_task_to_user(username, "task3")

   
        tasks = len(self.todo.get_users_tasks(username))
        self.assertEqual(tasks, 3)

        self.assertIsNone(self.todo.get_users_tasks("non_existent_user"))

    # ChatGpt apuna käyttäen
    def test_get_users_done_tasks(self):
        
        self.todo.create_user("john_doe", "password", signin=True)
        self.todo.add_task_to_user("john_doe", "Task 1")
        self.todo.add_task_to_user("john_doe", "Task 2")
        self.todo.change_user_task_status("john_doe", "Task 1")
        done_tasks = self.todo.get_users_done_tasks("john_doe")

        self.assertEqual(len(done_tasks), 1)
       


    def test_get_users_undone_tasks(self):
    
        user = self.todo.create_user("Yuusuf", "password", signin=True)
        self.todo.add_task_to_user("Yuusuf", "Heitä roskat")
        undone_tasks = self.todo.get_users_undone_tasks("Yuusuf")
        self.assertEqual(len(undone_tasks), 1)
        self.assertEqual(undone_tasks[0], "Heitä roskat")

    # ChatGpt apuna käyttäen
    def test_remove_task_from_user(self):
        tasks = self.todo.get_users_tasks("Yuusuf")
        count = len(tasks)
        self.todo.add_task_to_user('Yuusuf', "Read")
        self.todo.remove_task_from_user('Yuusuf', "Read")
        self.assertEqual(count, 1)


       

    # ChatGpt apuna käyttäen
    def test_user_tasks_status_changes(self):
        self.todo.create_user("Jaja", "password", signin=True)
        self.todo.add_task_to_user("Jaja", "Nuku")
      
        tasks = self.todo.get_users_undone_tasks("Jaja")
        self.assertEqual(len(tasks), 1)
        self.todo.change_user_task_status('Jaja', "Nuku")
        tasks2 = self.todo.get_users_done_tasks('Jaja')
        self.assertEqual(len(tasks), 1)
            
    def test_change_task_priority(self):
        self.todo.create_user("maca", "test_password", signin=True)
        self.todo.add_task_to_user("maca", "task1")
        self.todo.change_task_priority("maca", "task1", "high")
        tasks = self.todo.get_users_tasks("maca")

        for task in tasks:
            print(task)
            if task[0] == "task1":
                self.assertEqual(task[2], "high")
                break
        else:
            self.fail("Task not found")
