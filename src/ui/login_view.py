from tkinter import ttk, StringVar, constants
from service.user_service import UserService, CredentialsBeingIncorrect, UsernameTakenError, user_service

class LoginView:

    """Class representing the login view of the Todo application.
        """    

    def __init__(self, master, manage_login, manage_create_user_view):
        """Initializes LoginView instance.

        Args:
            master (tkinter.Tk): The root window of the application.
            manage_login (function): Function to call when login is successful.
            manage_create_user_view (function): Function to call when create user view is requested.
        """
        self.master = master
        self.manage_login = manage_login
        self.manage_create_user_view = manage_create_user_view

        self.frame = None
        self.indentification_entry = None
        self.matchword_entry = None
        self.error_variable = None
        self.error_label = None
        self.assign()


    def pack(self):
        """Packs the login view frame."""
        self.frame.pack(fill=constants.X)

    def dismantle(self):
        """destroyes login view frame"""
        self.frame.destroy()


    def login_manager(self):
        """Calls user_service to check user and initiate login only when successful. 
        Displays error message if check up fails."""
        username = self.indentification_entry.get()
        password = self.matchword_entry.get()
    
        try:
            user_service.signin(username, password)
            self.manage_login()

        except CredentialsBeingIncorrect:
            self.show_error("Invalid username or password")

    
    def show_error(self, message):
        """Displays error message on the login view.

        Args:
            message (str): The error message to be shown.
        """
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        """Hides error message on the login view."""
        self.error_label.grid_remove()

    def setup_username_domain(self):
        """Sets up username domain of the login view."""
        header_label = ttk.Label(
            master=self.frame,
            text="Welcome",
            font=("System", 12))

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=constants.W)
        
        username_label = ttk.Label(master=self.frame, text="Username:", font=("System", 10))
        self.indentification_entry = ttk.Entry(master=self.frame, style="Custom.TEntry")
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.indentification_entry.grid(padx=5, pady=5, sticky=constants.EW)

    
    def setup_password_domain(self):
        """Sets up password domain of the login view."""
        password_label = ttk.Label(master=self.frame, text="Password:", font=("System", 10))
        self.matchword_entry = ttk.Entry(master=self.frame, show="*", style="Custom.TEntry")
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.matchword_entry.grid(padx=5, pady=5, sticky=constants.EW)


    def assign(self):
        """ Assigns the necessary widgets and attributes to the view."""
        self.frame = ttk.Frame(master=self.master)
        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground="red")

        self.error_label.grid(padx=5, pady=5)

        self.setup_username_domain()
        self.setup_password_domain()

        login_button = ttk.Button(
            master=self.frame,
            text="Sign in",
            command=self.login_manager,
            style="Custom.TButton"
        )

        create_user_button = ttk.Button(
            master=self.frame,
            text="Sign up",
            command=self.manage_create_user_view,
            style="Custom.TButton"
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.hide_error()

        
        self.master.style = ttk.Style(self.master)
        self.master.style.theme_use('clam')

        self.master.style.configure('Custom.TButton', 
                                    background='#FFC107', 
                                    foreground='black',
                                    padding=10, 
                                    font=('Helvetica'))
       
