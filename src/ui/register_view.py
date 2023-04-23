from tkinter import ttk, StringVar, constants
from service.todo_service import TodoApp, InvalidCredentialsError, UsernameExistsError, app_service

class RegisterView:
    def __init__(self, master, manage_register, manage_login_view):
        self.master = master
        self.manage_register = manage_register
        self.manage_login_view = manage_login_view

        self.frame = None
        self.indentification_entry = None
        self.matchword_entry = None
        self.error_variable = None
        self.error_label = None
        
        self.initialize()


    def pack(self):
        self.frame.pack(fill=constants.X)

    def dismantle(self):
        self.frame.destroy()


    def create_user_manager(self):
        username = self.indentification_entry.get()
        password = self.matchword_entry.get()

        if len(username) == 0 or len(password) == 0:
            self.show_error("Username and password is required")
            return
    
        try:
            app_service.create_user(username, password, signin=True)
            self.manage_register()

        except UsernameExistsError:
            self.show_error(f"Username {username} already exists")

    
    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def setup_username_domain(self):

        username_label = ttk.Label(master = self.frame, text="Username:")
        self.indentification_entry = ttk.Entry(master=self.frame)
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.indentification_entry.grid(padx=5, pady=5, sticky=constants.EW)

    
    def setup_password_domain(self):

        password_label = ttk.Label(master = self.frame, text="Password:")
        self.matchword_entry = ttk.Entry(master=self.frame)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.matchword_entry.grid(padx=5, pady=5, sticky=constants.EW)


    def initialize(self):
        self.frame = ttk.Frame(master=self.master)
        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground="red")

        self.error_label.grid(padx=5, pady=5)

        self.setup_username_domain()
        self.setup_password_domain()

        register_user_button = ttk.Button(
            master=self.frame,
            text="Register",
            command=self.create_user_manager
        )

        login_button = ttk.Button(
            master=self.frame,
            text="Login",
            command=self.manage_login_view
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)

        register_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.hide_error()