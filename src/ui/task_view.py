from tkinter import ttk, constants
from service.todo_service import TodoApp,app_service
import datetime
class Users_tasklist_view:
    def __init__(self, master, tasks, manage_task_status):

        self.master = master
        self.tasks = tasks
        self.manage_task_status = manage_task_status
        self.frame = None

        self.assign()


    def dismantle(self):
        self.frame.destroy()



    def pack(self):
        self.frame.pack(fill=constants.X)

    def assign_task_status(self, task):
        item_frame = ttk.Frame(master=self.frame)
        update_label = ttk.Label(master=item_frame, text=str(task))

        update_task_button = ttk.Button(
            master=item_frame,
            text="Done",
            command=lambda: self.manage_task_status(task),
            style="Custom.TButton"
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

       
    def assign(self):
        self.frame = ttk.Frame(master=self.master)
        if self.tasks != None:
            for task in self.tasks:
                self.assign_task_status(task)

class TaskView:
    def __init__(self, master, handle_logout):
        self.master = master
        self.handle_logout = handle_logout
        self.user = app_service.get_current_user()
        self.frame = None
        self.create_todo_entry = None
        self.todo_list_frame = None
        self.task_list_view = None
        self.assign()        

        
    def pack(self):
        self.frame.pack(fill=constants.X)

    def dismantle(self):
        self.frame.destroy()

    def logout_manage(self):
        app_service.logout()
        self.handle_logout()

    def manage_task_status(self, task):
        app_service.change_user_task_status(self.user.name, task)
        self.frame.after(100, lambda: self.assign_todo_list(self.user.name))


    def time_of_creation(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")


        
    def assign_todo_list(self, name):
        if self.task_list_view:
            self.task_list_view.dismantle()
            
        tasks = app_service.get_users_undone_tasks(name)

        self.task_list_view = Users_tasklist_view(
            self.todo_list_frame,
            tasks,
            self.manage_task_status
        )

        self.task_list_view.pack()



    def assign_header(self):
        user_icon = ttk.Label(
            master=self.frame,
            text=f"Logged in as {self.user.name}"
        )

        logout_icon = ttk.Button(
            master=self.frame,
            text="Logout",
            command=self.logout_manage,
            style="Custom2.TButton"
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
            now = self.time_of_creation()
            app_service.add_task_to_user(self.user.name,f"{todo_content} ({now})")
            self.create_todo_entry.delete(0, constants.END)
            self.assign_todo_list(self.user.name)
            success_label = ttk.Label(
                master=self.frame,
                text="Task created successfully!",
                style="Success.TLabel"
            )
            success_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)
            self.frame.after(3000, success_label.destroy)



    def assign_footer(self):
        input_frame = ttk.Frame(master=self.frame, padding=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=0)
        input_frame.columnconfigure(2, weight=0)

        input_label = ttk.Label(master=input_frame, text="New Task:")

        self.create_todo_entry = ttk.Entry(master=input_frame, font=("TkDefaultFont", 12))
        self.create_todo_entry.grid(row=0, column=0, padx=5, pady=5, sticky=constants.EW)

        create_todo_button = ttk.Button(
            master=input_frame,
            text="Add Task",
            command=self.handle_create_todo,
            style="Custom.TButton",
            padding=10,
        )
        create_todo_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)

        input_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        ttk.Separator(master=self.frame, orient="horizontal").grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=10
        )
        input_frame.grid(row=3, column=0, padx=10, pady=10, sticky=constants.EW)

        self.create_todo_entry.focus_set()



    def assign(self):
        self.frame = ttk.Frame(master=self.master)
        self.todo_list_frame = ttk.Frame(master=self.frame)

        self.assign_header()
        self.assign_todo_list(self.user.name)
        self.assign_footer()

        self.todo_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)
        self.frame.grid_columnconfigure(1, weight=0)



        self.master.style.configure('Custom.TButton', 
                                    background='#FFC107', 
                                    foreground='black',
                                    padding=10, 
                                    font=('Helvetica'))

        self.master.style.configure('Custom2.TButton', 
                                    background='#FF5207', 
                                    foreground='black',
                                    padding=10, 
                                    font=('Helvetica'))
            
    
        self.master.style.configure('Success.TLabel',
                            background='#4CAF50',
                            foreground='white',
                            padding=5,
                            font=('Helvetica', 12, 'bold'))