#from UI import login_view
from entities.todo import Todo
from entities.user import User

#todo_tietokanta.create_tables()

yusuboi = User("yusuboi", "rakastansql")



todo1 = Todo("Siivoa huone")

yusuboi.create_todo(todo1)


"""
yusuboi.todos: [(
todo1   
    todo1.text: Siivoa huone
    todo1.completed: False    
)]
"""

for todo in yusuboi.todos:
    print(todo.completed)