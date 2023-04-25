# **Arkkitehtuurikuvaus**
## **Sovelluslogiikka**

User-luokka sisältää käyttäjän nimen, salasanan ja viittauksen käyttäjän tehtävälistaan (TaskList). Tehtävälista sisältää luettelon tehtävistä (Task). Jokaisella tehtävällä on nimi ja tila, joka kertoo onko tehtävä suoritettu vai ei.
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


****
## **Sekvenssikaavio**

```mermaid
sequenceDiagram
  actor Registered User
  participant ui
  participant TodoApp
  participant UserDatabase

  Registered User->>ui: click "Sign in" button
  ui->>TodoApp: signin("Yuusuf", "SQLlover")
  TodoApp ->>TodoApp: get_user_by_username("Yuusuf")
  TodoApp->>UserDatabase: find_by_username("Yuusuf")
  UserDatabase-->>TodoApp: user
  TodoApp-->>ui: user
  ui->ui: display_tasks_view()
```
