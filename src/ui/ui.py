from ui.login_view import LoginView
from ui.register_view import RegisterView

class UI:
    def __init__(self, master):
        self.master = master
        self.current_outlook = None

    def initate(self):
        self.display_login_view()
    
    def  hide_current_outlook(self):
        if self.current_outlook:
            self.current_outlook.destroy()

        self.current_outlook = None

    def display_login_view(self):
        self.hide_current_outlook()

        self.current_outlook = LoginView(self.master, self.display_register_view)
        self.current_outlook.pack()





    def display_register_view(self):
        pass
