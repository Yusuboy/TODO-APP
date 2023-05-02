from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.task_view import Users_tasklist_view, TaskView

class UI:
    """
    A class that manages user interface of the Todo application.

    Attributes:
        master: The root window of the application.
        current_outlook: The currently displayed view.

    Methods:
        initate(): Initializes the user interface by displaying the login view
        hide_current_outlook(): Hides the current view if it exists
        display_login_view(): Displays the login view
        display_tasks_view(): Displays the users task list view
        display_create_user_view(): Displays the register view for creating a new user

    """
    def __init__(self, master):

        """
        Initializes a new ccurrence of the UI class.

        Args:
            master: The root window of the application.
        """
        self.master = master
        self.current_outlook = None

    def initate(self):
        """
        Initializes the user interface by displaying the login view.

        """
        self.display_login_view()
    
    def hide_current_outlook(self):
        """
        Hides the current view if it exists.
        """
        
        if self.current_outlook:
            self.current_outlook.dismantle()

        self.current_outlook = None


    def display_login_view(self):
        """
        Displays the login view.
        """
        self.hide_current_outlook()

        self.current_outlook = LoginView(
            self.master,
            self.display_tasks_view,
            self.display_create_user_view
        )

        self.current_outlook.pack()


    def display_tasks_view(self):
        """
        Displays the task view.
        """
        self.hide_current_outlook()

        self.current_outlook = TaskView(self.master, self.display_login_view)

        self.current_outlook.pack()


    
    def display_create_user_view(self):
        """
        Displays the create user view.
        """
        
        self.hide_current_outlook()

        self.current_outlook = RegisterView(
            self.master,
            self.display_tasks_view,
            self.display_login_view
        )

        self.current_outlook.pack()