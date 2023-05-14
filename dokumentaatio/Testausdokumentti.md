# **Testausdokumentti**
Ohjelman toimivuutta on varmistettu sekä automatisoiduilla yksikkö- ja integraatiotesteillä käyttäen unittestia että manuaalisesti suoritetuilla järjestelmätason testeillä.

## Yksikkö- ja integraatiotestauksen suorittaminen
***
### **Sovelluslogiikka**
Sovelluslogiikasta vastaa TodoService-luokka sekä UserService-luokat. Test_todo_service-testiluokka varmistaa TodoService-luokan toimivuuden tarkistamalla sovelluslogiikan oikeellisuuden. Test_user_service-testiluokka taas varmistaa UserServicen-luokan toimivuuden. Integraatiotesti tasolla Test_todo_service-testiluokka sekä Test_user_service-testiluokka varmistavat myös repositorien luokkien, UserDatabase ja TaskDatabase toimivuutta.
UserDatabase-luokan toiminnallisuutta testataan lisäksi myös Test_UserDatabase-testiluokan avulla.

### **Testauskattavuus**
Ottamatta huomioon ui luokkia, sovelluksen testauksen haarautumakattavuus on 99%
![Kuva](./Kuvat/Testikattavuus.png)
Testikattavuuden ulkopuolelle jätettiin build.py

## Järjestelmätestaus
***
Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.
### **Asennus ja konfigurointi**

Sovellus on läpikäynyt onnistuneen lataus- ja testausprosessin macOS- ja Linux-käyttöjärjestelmissä [käyttöohjeessa](./Käyttöohje.md) kuvatulla tavalla. Testaus on toteutettu käyttäen erilaisia konfiguraatioita, jotka on määritelty tarkasti .env-tiedostossa.

## Sovellukseen jääneet laatuongelmat
Emme saaneet näkyväksi Todo prioriteettia käyttöliittymässä. Jokaiselle todolla prioriteetti ja prioriteetti voidaan valita, jolloin se näkyy tietokannassa, mutta sen näyttäminen käyttöliittymässä ei onnistunut.