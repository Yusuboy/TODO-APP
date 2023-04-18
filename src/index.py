from initialize_database import drop_table
from service.todo_service import TodoApp



user = TodoApp()

user.create_user("Yusuf", 'password')
user.get_user_by_username("Yuusuf")
user.add_task_to_user("Yusuf", "task")
user.get_users_tasks("Yuusuf")
user.get_users_undone_tasks("Yuusuf")
user.change_user_task_status("Yuusuf", "task")
user.get_users_done_tasks("Yuusuf")
user.remove_task_from_user("Yuusuf", "task")