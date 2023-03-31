
```mermaid
---
title: Monopoly
---
classDiagram

    Pelilauta <|-- Nopat
    Pelilauta <|-- Rakentaminen
    Ruudut    <|-- Normaalikatu
    Pelaaja   <|-- Raha
    note for Pelaaja "Pelaajilla on rahaa"

    Normaalikatu <|-- Rakentaminen
    Pelaaja <|.. Normaalikatu
    not for Pelaaja "Pelaaja voi omistaa kadun"

    note for Rakentaminen "Normaali katu-ruutuihin voidaan rakentaa korkeintaa 4 taloa tai yhden hotellin"
    note for Nopat "Pelataan käyttäen kaksi noppaa"
    Pelilauta <|-- Pelaajat
    Ruudut    <|-- Kortit 
    note for Kortit "Sattuma -ja yhteismaaruutuihin liittyy kortteja, johon liittyy joku toiminto"
    Ruudut  <|-- Toiminta
    note for Toiminta "Toimintoja on useanlaisia"
    note for Pelaajat "Pelaajia vähintään 2 ja enintään 8"
    note for Pelaajat "Jokaisella pelajaalla on yksi pelinappula"
    Pelilauta <|-- Ruudut
    note for Pelilauta "Pelilautoja ainoastaan yksi\npelilauta sisältää 40 ruutua"
    note for Ruudut "Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla.\Ruutuja useampi eri tyyppejä:\Aloitusruutu\Vankilaruutu\Sattuma- ja Yhteismaaruutu\Asema -ja laitosruutu ruudut\Normaalit kadut (joihin liittyy nimet) ruudut"
    note for Pelilauta "ALoitusruudun ja vankilaruudun sijainti tiedossa"

    Pelilauta <|-- Pelinappulat
    note for Pelinappulat "Pelinappula sijaitsee aina yhdessä ruudussa"
    Pelaajat  <|-- Pelinappulat
    Ruudut    <|-- Pelinappulat
    
```