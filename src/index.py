import tkinter as tk
from ui.login_view import LoginView
root = tk.Tk()

def manage_login():
    # Code to switch to the main to-do list view
    pass

def manage_create_user_view():
    # Code to switch to the create user view
    pass

login_view = LoginView(root, manage_login, manage_create_user_view)
login_view.pack()

root.mainloop()