from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.task_view import Users_tasklist_view, TaskView

class UI:
    def __init__(self, master):
        self.master = master
        self.current_outlook = None

    def initate(self):
        self.display_login_view()
    
    def hide_current_outlook(self):
        if self.current_outlook:
            self.current_outlook.dismantle()

        self.current_outlook = None


    def display_login_view(self):
        self.hide_current_outlook()

        self.current_outlook = LoginView(
            self.master,
            self.show_todos_view,
            self.show_create_user_view
        )

        self.current_outlook.pack()


    def show_todos_view(self):
        self.hide_current_outlook()

        self.current_outlook = TaskView(self.master, self.display_login_view)

        self.current_outlook.pack()


    
    def show_create_user_view(self):
        self.hide_current_outlook()

        self.current_outlook = RegisterView(
            self.master,
            self.show_todos_view,
            self.display_login_view()
        )

        self.current_outlook.pack()