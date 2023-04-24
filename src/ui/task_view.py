from tkinter import ttk, constants
from service.todo_service import TodoApp,app_service

class Users_tasklist_view:
    def __init__(self, master, todos, manage_task_status):

        self.master = master
        self.todos = todos
        self.manage_task_status = manage_task_status
        self.frame = None

        self.initialize()


    def dismantle(self):
        self.frame.destroy()



    def pack(self):
        self.frame.pack(fill=constants.X)

    def initialize_task_status(self, todo):
        item_frame = ttk.Frame(master=self.frame)
        update_label = ttk.Label(master=item_frame, text=str(todo))

        update_task_button = ttk.Button(
            master=item_frame,
            text="Done",
            command=lambda: self.manage_task_status(todo)
        )

        update_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        update_task_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

       
    def initialize(self):
        self.frame = ttk.Frame(master=self.master)
        if self.todos != None:
            for todo in self.todos:
                self.initialize_task_status(todo)

class TaskView:
    def __init__(self, master, handle_logout):
        self.master = master
        self.handle_logout = handle_logout
        self.user = app_service.get_current_user()
        self.frame = None
        self.create_todo_entry = None
        self.todo_list_frame = None
        self.task_list_view = None
        self.initialize()        

        
    def pack(self):
        self.frame.pack(fill=constants.X)

    def dismantle(self):
        self.frame.destroy()

    def logout_manage(self):
        app_service.logout()
        self.handle_logout()

    def manage_task_status(self, task):
        app_service.change_user_task_status(self.user.name, task)
        self.initialize_todo_list(self.user.name)

        
    def initialize_todo_list(self, name):
        if self.task_list_view:
            self.task_list_view.dismantle()
            
        todos = app_service.get_users_undone_tasks(name)

        self.task_list_view = Users_tasklist_view(
            self.todo_list_frame,
            todos,
            self.manage_task_status
        )

        self.task_list_view.pack()



    def initialize_header(self):
        user_icon = ttk.Label(
            master=self.frame,
            text=f"Logged in as {self.user.name}"
        )

        logout_icon = ttk.Button(
            master=self.frame,
            text="Logout",
            command=self.logout_manage
        )

        user_icon.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_icon.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
   
        )


    def handle_create_todo(self):
        todo_content = self.create_todo_entry.get()

        if todo_content:
            app_service.add_task_to_user(self.user.name,todo_content)
            self.initialize_todo_list(self.user.name)
            self.create_todo_entry.delete(0, constants.END)


    def initialize_footer(self):
        self.create_todo_entry = ttk.Entry(master=self.frame)

        create_todo_button = ttk.Button(
            master=self.frame,
            text="Create",
            command=self.handle_create_todo
        )

        
        self.create_todo_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        create_todo_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )


    def initialize(self):
        self.frame = ttk.Frame(master=self.master)
        self.todo_list_frame = ttk.Frame(master=self.frame)

        self.initialize_header()
        self.initialize_todo_list(self.user)
        self.initialize_footer()

        self.todo_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)
        self.frame.grid_columnconfigure(1, weight=0)
