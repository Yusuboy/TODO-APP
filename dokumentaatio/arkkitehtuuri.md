```mermaid
 classDiagram
      Task "*" --> "1" User
      class User{
          name: str
          password: str
          tasklist: Tasklist
      }
      class Todo{
          name: str
          completed: bool
      }
``