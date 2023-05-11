### Viikko 3
-Lisätty Level-luokka, joka vastaa ruudukon muodostamisesta

-Lisätty muutama sprite-luokka

-Määritelty main-funktio

-Peli muodostaa 9x9 ruudukon ja näyttää 10 miinan paikan

-Vasen-klikkaamalla miinaa peli päättyy

-Oikea-klikkaus asettaa ruutuun lipun, mutta grafiikka ei näy vielä

-Testattu, että Level-luokan parametrit määräytyvät oikein
### Viikko 4
-Peli toimii olennaisin osin (Ruutuja pystyy paljastamaan ja lippuja asettamaan, kaikkien ruutujen paljastaminen ja miinojen löytäminen johtaa voittoon, miinan klikkaaminen häviöön)

-Sovelluksen saa lopetettua painamalla esciä

-Koodia paranneltu pylint-ohjeiden mukaan

### Viikko 5
-Pelin perusominaisuudet valmiit (nyt isompi osa ruudukosta paljastuu, jos ruudun ympärillä ei ole miinoja)

-Ensimmäisestä klikatusta ruudusta ei löydy miinaa

-Ulkonäköä paranneltu, paljastetut ruudut näkyvät selkeämmin ja kursorin alla oleva ruutu erottuu erivärisenä

### Viikko 6
-Pelin vaikeusasteen pystyy valitsemaan (helppo, keskivaikea, vaikea)

-Pelin voi aloittaa alusta "r"-napilla (senhetkinen vaikeusaste)

-Uusi sprite löydetylle miinalle

### Viikko 7
-Pelissä on laskuri merkatuille miinoille

-Pelissä on ajastin

-Luotu SQL-tietokanta, joka pitää kirjaa ennätyksistä

-Käyttöliittymää muutettu: jokaisen pelin päätteeksi näkee ennätyslistan ja näppäinkomennot

-Testattu, että

+ Peliä ei voi voittaa väärinasetetuilla lipuilla
+ Lippuja ei voi asettaa pelin loputtua
+ Paljastettua ruutua ei voi paljastaa uudelleen
+ Jos paljastetun ruudun ympärillä ei ole miinoja, myös nämä ruudut ovat paljastuneet
