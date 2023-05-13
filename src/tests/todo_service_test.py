import unittest
from service.user_service import UserService, UsernameTakenError, CredentialsBeingIncorrect
from service.task_service import TodoService, todo_service
from entities.tasks import Task

class Test_todo_service(unittest.TestCase):
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

       
    
    def test_add_task_to_user(self):
        taskit = Task("Hellou", 'high')
        taskit2 = Task("Hellouu2", 'high')
        self.person.create_user("Pekka", "password", signin=True)
        self.task.add_task_to_user('Pekka', taskit)
        Tasks = self.task.get_users_tasks("Pekka")
        count1 = len(Tasks)
        self.task.add_task_to_user("Pekka", taskit)
        Tasks2 = self.task.get_users_tasks("Pekka")
        count2 = len(Tasks2)
        self.assertNotEqual(count1, count2)
        self.assertIsNone(self.task.add_task_to_user("Pekka2", taskit2))

      

    
    def test_get_users_tasks(self):
   
        username = "test_user"
        password = "test_password"
        taskit1 = Task('task1', 'high')
        taskit3 = Task('task1', 'high')
        taskit4 = Task('task1', 'high')

        self.person.create_user(username, password, signin=True)
        self.task.add_task_to_user(username, taskit1)
        self.task.add_task_to_user(username, taskit3)
        self.task.add_task_to_user(username, taskit4)

   
        tasks = len(self.task.get_users_tasks(username))
        self.assertEqual(tasks, 3)

        self.assertIsNone(self.task.get_users_tasks("non_existent_user"))

    # ChatGpt apuna käyttäen
    def test_get_users_done_tasks(self):
        taskit1 = Task('task1', 'high')
        taskit2 = Task('task2', 'high')
        
        self.person.create_user("john_doe", "password", signin=True)
        self.task.add_task_to_user("john_doe", taskit1)
        self.task.add_task_to_user("john_doe",  taskit2)
        self.task.change_user_task_status("john_doe", "task1")
        done_tasks = self.task.get_users_done_tasks("john_doe")

        self.assertEqual(len(done_tasks), 1)
       


    def test_get_users_undone_tasks(self):
        taskit1 = Task('task1', 'high')
        

        user = self.person.create_user("Yuusuf", "password", signin=True)
        self.task.add_task_to_user("Yuusuf", taskit1)
        undone_tasks = self.task.get_users_undone_tasks("Yuusuf")
        self.assertEqual(len(undone_tasks), 1)
        self.assertEqual(undone_tasks[0],'task1')

    # ChatGpt apuna käyttäen
    def test_remove_task_from_user(self):
        taskit1 = Task('task1', 'high')
        tasks = self.task.get_users_tasks("Yuusuf")
        count = len(tasks)
        self.task.add_task_to_user('Yuusuf', taskit1)
        self.task.remove_task_from_user('Yuusuf', "task1")
        self.assertEqual(count, 1)


       

    # ChatGpt apuna käyttäen
    
    def test_user_tasks_status_changes(self):
        taskit2 = Task('task2', 'high')
        self.person.create_user("Jaja", "password", signin=True)
        self.task.add_task_to_user("Jaja", taskit2)
      
        tasks = self.task.get_users_undone_tasks("Jaja")
        self.assertEqual(len(tasks), 1)
        self.task.change_user_task_status('Jaja', "task2")
        tasks2 = self.task.get_users_done_tasks('Jaja')
        self.assertEqual(len(tasks), 1)
            
    def test_change_task_priority(self):
        taskit2 = Task('task2', 'high')
        self.person.create_user("maca", "test_password", signin=True)
        self.task.add_task_to_user("maca", taskit2)
        self.task.change_task_priority("maca", "task2", "medium")
        tasks = self.task.get_users_tasks("maca")

        for task in tasks:
            if task[0] == "task2":
                self.assertEqual(task[2], "medium")
                break
        else:
            self.fail("Task not found")
