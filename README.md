
# TODO-APP
Todo-appi on älykäs sovellus, jonka avulla käyttäjä voit hallita tehtävälistojaan ja tarkastella päivittäisiä tehtäviään helposti ja vaivattomasti. Sovellus tarjoaa monipuolisia toimintoja, kuten tehtävälistojen luonti ja merkintä tehtävien suorittamisesta sekä priorisoinnin. Todo-apilla voit luoda selkeitä listoja tehtävistäsi, jolloin sinun on helppo pitää yllä tärkeitä asioitasi. Kun olet suorittanut tehtävän, voit merkitä sen kätevästi suoritetuksi Todo-appin avulla.

***
## **Dokumentaatio**
- [Vaatimuusmaaritttely](dokumentaatio/vaatimusmaarittely.md)
- [Käyttöohje](dokumentaatio/Käyttöohje.md)
- [Changelog](dokumentaatio/changelog.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/Testausdokumentti.md)

****
## **[Release 1](https://github.com/Yusuboy/ot-harjoitustyo/releases/tag/Viikko5)**
## **[Release2](https://github.com/Yusuboy/ot-harjoitustyo/releases/tag/Viikko6)**
****

## **Asennus**
**0. Ennen asennusta siirry virtuaaliympäristöön komennolla:**
```bash
poetry shell
```

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
