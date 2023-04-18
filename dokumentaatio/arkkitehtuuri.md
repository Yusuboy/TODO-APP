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