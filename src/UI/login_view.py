import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Login")
        self.root
        
        tk.Label(text="Hello, Tkinter")
        # Create username label and entry widget
        tk.Label(self.root, text="Username: ").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)
        
        # Create password label and entry widget
        tk.Label(self.root, text="Password: ").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)
        
        # Create login button
        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.grid(row=2, column=1)
        
        # Create error message label
        self.error_message = tk.Label(self.root, text="", fg="red")
        self.error_message.grid(row=3, column=1)
        
        self.root.mainloop()
    
    def login(self):
        # TODO: Implement login functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "password":
            # Login successful, close the login window
            self.root.destroy()
            # TODO: Open the main to-do app window here
        else:
            # Login failed, display error message
            self.error_message.config(text="Invalid username or password")
            
if __name__ == '__main__':
    app = LoginView()
