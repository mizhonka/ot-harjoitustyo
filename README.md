# Miinaharava (Ot-harjoitustyö)

Pelissä on tarkoitus löytää piilotetut miinat ruudukosta numerovihjeiden perusteella. Voitat, kun kaikki miinat on merkitty ja tyhjät ruudut avattu!

## Dokumentaatio
[Käyttöohje](https://github.com/mizhonka/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/mizhonka/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/mizhonka/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/mizhonka/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/mizhonka/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asennus
[Uusin release](https://github.com/mizhonka/ot-harjoitustyo/releases/tag/viikko5)

1. Pura zip-tiedosto ja navigoi komentorivillä puretun hakemisto sisällä "miinaharava"-hakemistoon.

2. Asenna riippuvuudet komennolla
```
poetry install
```

3. Käynnistä sovellus komennolla
```
poetry run invoke start
```
## Komentorivitoiminnot
### Ohjelman suorittaminen
```
poetry run invoke start
```
### Testaus
```
poetry run invoke test
```
### Testikattavuus
```
poetry run invoke coverage-report
```
### Pylint-tarkistus
```
poetry run invoke lint
```
### Automaattinen formatointi
```
poetry run invoke format
```
