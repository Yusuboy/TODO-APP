from tkinter import Tk, ttk


root = Tk()
root.title("Todo App")




username_label = ttk.Label(root, text="Käyttäjänimi:")
username_label.pack()

username_entry = ttk.Entry(root)
username_entry.pack()

password_label = ttk.Label(root, text=" Käyttäjätunnus:")
password_label.pack()

password_entry = ttk.Entry(root, show="*")
password_entry.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()

   

login_button = ttk.Button(root, text="Kirjaudu", command=login)
login_button.pack()

root.mainloop()

