from tkinter import ttk, StringVar, constants
from service.user_service import UserService, CredentialsBeingIncorrect, UsernameTakenError, user_service, InvalidUsername

class RegisterView:
    """Class representing the view that allows user register for the Todo application.
        """   
    def __init__(self, master, manage_register, manage_login_view):
        """Initializes RegisterView instance.

        Args:
                master: The parent widget.
                manage_register: The function to call when the registration is complete.
                manage_login_view: The function to call when the user wants to switch to the login view.
        """
        self.master = master
        self.manage_register = manage_register
        self.manage_login_view = manage_login_view

        self.frame = None
        self.indentification_entry = None
        self.matchword_entry = None
        self.error_variable = None
        self.error_label = None
        
        self.assign()


    def pack(self):
        """Packs the register view frame."""
        self.frame.pack(fill=constants.X)

    def dismantle(self):
        """destroyes register view frame"""
        self.frame.destroy()


    def create_user_manager(self):
        """Calls user_service to check user and initiate login only when successful. 
        Displays error message if check up fails."""
        username = self.indentification_entry.get()
        password = self.matchword_entry.get()

        if len(username) == 0 or len(password) == 0:
            self.show_error("Username and password is required")
            return

        
        try:
            user_service.create_user(username, password, signin=True)
            self.manage_register()

        except UsernameTakenError:
            self.show_error(f"Username {username} already exists")

        except InvalidUsername:
            self.show_error("Username must be minimum of 4 characters")

    
    def show_error(self, message):
        """Displays error message on the register view.

        Args:
            message (str): The error message to be shown.
        """
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        """Hides error message on the register view."""
        self.error_label.grid_remove()

    def setup_username_domain(self):
        """Sets up username domain of the register view."""
        username_label = ttk.Label(master = self.frame, text="Username:")
        self.indentification_entry = ttk.Entry(master=self.frame, style="Custom.TEntry")
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.indentification_entry.grid(padx=5, pady=5, sticky=constants.EW)

    
    def setup_password_domain(self):
        """Sets up password domain of the register view."""
        password_label = ttk.Label(master = self.frame, text="Password:")
        self.matchword_entry = ttk.Entry(master=self.frame, show="*", style="Custom.TEntry")
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.matchword_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def backToLog(self):
        user_service.logout()
        self.manage_login_view()


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

        register_user_button = ttk.Button(
            master=self.frame,
            text="Register",
            command=self.create_user_manager,
            style="Custom.TButton"
        )

        back_button = ttk.Button(

            master=self.frame,
            text="Back",
            command=self.backToLog,
            style="Custom.TButton"
        )

        

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)

        register_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        back_button.grid(padx=1, pady=1, sticky=constants.EW)
       

        self.hide_error()

        self.master.style = ttk.Style(self.master)
        self.master.style.theme_use('clam')

        self.master.style.configure('Custom.TButton', 
                                    background='#FFC107', 
                                    foreground='black',
                                    padding=10, 
                                    font=('Helvetica'))
       