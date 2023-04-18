```mermaid
 classDiagram
      Task  -->  User
      Task -- Tasklist
      class User{
          name: str
          password: str
          tasklist: Tasklist
      }
      class Task{
          name: str
          completed: bool
      }
      class Tasklist {
        tasks: list
      }
```