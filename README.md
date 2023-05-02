
# TODO-APP
- Todo-appi on sovellus, joka auttaa käyttäjää pitämään yllä tehtävälistaa ja organisoimaan päivittäisiä tehtäviään. Joitakin esimerkkejä siitä, mitä todo-apilla voidaan tehdä, ovat: Luoda tehtävälista: Todo-apilla voit luoda luettelon tehtävistä, jotka sinun täytyy suorittaa. Merkitä tehtävä suoritetuksi: Kun olet suortittanut tehtävän niin voit merkitä  sen suoritetuksi

***
## **Dokumentaatio**
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Vaatimuusmaaritttely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](dokumentaatio/Käyttöohje.md)
****
## **[Release 1](https://github.com/Yusuboy/ot-harjoitustyo/releases/tag/Viikko5)**
## ** [Release2](https://github.com/Yusuboy/ot-harjoitustyo/releases/tag/Viikko6)**
****
## **Asennus**
 **1. Asenna riippuvuudet komennolla:**
```bash
poetry install
```

 **2. Suorita vaadittavat alustoimenpiteet komennolla:**
```bash
poetry run invoke build
``` 

 **3. Sovelluksen voi käynnistää komennolla:**
```bash
poetry run invoke start
```
****

## **Komentorivi toiminnot**

### **Ohjelman suorittaminen**

 **Ohejelman voi käynistää komennolla:**
```bash
poetry run invoke start
```

### **Testaus**

**Testit suoritetaan komennollla:**
```bash
poetry run invoke test
```

### **Testikattavuus**
**Testikattavuusraportin voi generoida komennolla:**
```bash
poetry run invoke coverage-report
```

### **Pylint**
**Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:**
```bash
poetry run invoke lint
```
