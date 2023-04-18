import tkinter as tk
from ui.login_view import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    login_view = LoginView(root)
    root.mainloop()