import tkinter as tk

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        # Create username label and entry
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        # Create password label and entry
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        # Create login button
        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Perform login validation logic here
        print("Username:", username)
        print("Password:", password)

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    login_view = LoginView(root)
    root.mainloop()
