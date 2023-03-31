
```mermaid
---
title: Monopoly
---
classDiagram

    Pelilauta <|-- Nopat
    Pelilauta <|-- Pelaajat
    Pelilauta <|-- Rakentaminen
    Pelilauta <|-- Ruudut
    Ruudut    <|-- Normaalikatu
    Pelaajat   <|-- Raha
    Pelaajat   <|.. Normaalikatu
    Normaalikatu <|-- Rakentaminen
    Ruudut    <|-- Kortit 
    Ruudut    <|-- Toiminta
    Pelilauta <|-- Pelinappulat
    Pelaajat  <|-- Pelinappulat
    Ruudut    <|-- Pelinappulat
    


    note for Pelaajat "Pelaajilla on rahaa"
    not for Pelaajat "Pelaaja voi omistaa kadun"
    note for Rakentaminen "Normaali katu-ruutuihin voidaan rakentaa korkeintaa 4 taloa tai yhden hotellin"
    note for Nopat "Pelataan käyttäen kaksi noppaa"
    note for Kortit "Sattuma -ja yhteismaaruutuihin liittyy kortteja, johon liittyy joku toiminto"
    note for Toiminta "Toimintoja on useanlaisia"
    note for Pelaajat "Pelaajia vähintään 2 ja enintään 8"
    note for Pelaajat "Jokaisella pelajaalla on yksi pelinappula"
    note for Pelilauta "Pelilautoja ainoastaan yksi\npelilauta sisältää 40 ruutua"
    note for Ruudut "Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla\Ruutuja useampi eri tyyppejä"
    note for Pelilauta "ALoitusruudun ja vankilaruudun sijainti tiedossa"
    note for Pelinappulat "Pelinappula sijaitsee aina yhdessä ruudussa"
    
    
```