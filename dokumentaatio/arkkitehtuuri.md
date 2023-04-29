# Arkkitehtuurikuvaus

## Rakenne
Koodi on pakattu seuraavasti:
![Model](https://github.com/mizhonka/ot-harjoitustyo/blob/main/dokumentaatio/pakkausrakenne.png)
sprites-pakkaus sisältää pelissä käytettävät spritet ja on riippuvainen assets-pakkauksesta, joka sisältää png-grafiikat. ui-pakkaus sisältää käyttöliittymän ja hyödyntää sprites-pakkausta.
## Käyttöliittymä
Peli sisältää tällä hetkellä kaksi näkymää:
+ Vaikeusaste-valikko, josta vastaa Game-luokka
+ Itse peli, josta vastaa Level-luokka
## Sovelluslogiikka
Pelin alkaessa Game-luokan main-funktio luo uuden Level-olion. while-silmukka pyörii niin kauan kun running-muuttujan arvo on tosi. Joka silmukassa:
+ Level-oliosta kutsutaan Hover-metodia parametreina kursorin sijainti
+ Kutsutaan Level-oliosta joko reveal- tai draw_flag-metodi
+ Kutsutaan Level-oliosta init_sprites ja all_sprites.draw()
![Model](https://github.com/mizhonka/ot-harjoitustyo/blob/main/dokumentaatio/sekvenssi.png)
