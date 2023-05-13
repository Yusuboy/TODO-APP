# **Arkkitehtuurikuvaus**

## **Rakenne**
Koodin pakkaus rakenne on seuraavanlainen

![Kuva](./Kuvat/ohte_kaavio.png) 

ui sisältää tietoa käyttöliittymästä, services sisältää  tietoa sovelluslogiikasta ja repositories vastaa pysyvätallennuksesta. Pakkaus entities sisältää luokat user, tasks, tasklist jotka kuvastavat tietokohteita, jota sovelluskäyttää.
****
## **Käyttöliittymä**
Sovelluksemme käyttöliittymä sisältää kolme näkymää: Kirjautumisnäkymä, rekisteröitymisnäkymä ja tehtävälistalista näkymä. Jokainen näistä näkymistä ollaan toteutettu omissa luokissa. Näkymistä vastaa UI luokka. Käyttöliittymä kutsuu ainoastaan TaskService-luokan  sekä UserService-luokan metodeja.







## **Sovelluslogiikka**

User-luokka sisältää käyttäjän nimen ja salasanan. Jokaisella tehtävällä on nimi ja tila, joka kertoo onko tehtävä suoritettu vai ei.
```mermaid
 classDiagram
      Task  -->  User
      
      
      class User{
          name: str
          password: str
      }
      class Task{
          name: str
          completed: bool
      }
      
```


****
## **Sekvenssikaavio**

```mermaid
sequenceDiagram
  actor Registered User
  participant ui
  participant UserService
  participant UserDatabase

  Registered User->>ui: click "Sign in" button
  ui->>UserService: signin("Yuusuf", "SQLlover")
  UserService->>UserDatabase: find_by_username("Yuusuf")
  UserDatabase-->>UserService: user
  UserService-->>ui: user
  ui->ui: display_tasks_view()
```
