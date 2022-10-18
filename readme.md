# Työohje

Toteuta ohjelmoimalla yhtälön numeerinen ratkaisumenetelmä. Voit valita haluatko toteuttaa puolitusmenetelmän vai kiintopistemenetelmän.

## Puolitusmenetelmä

![Puolitusmenetelmä](./puolitusmenetelma.PNG)

## Kiintopistemenetelmä

![Kiintopistemenetelmä](./kiintopistemenetelma.PNG)

## Arviointi

Ihan ok:

- Ohjelma osaa ratkaista yhtälön $x - \cos{x} = 0$ numeerisesti halutulla tarkkuudella
- Ohjelmaan kirjoitetaan alkuarvaus / aloitusväli esim. Geogebran kuvan perusteella
- Ohjelma tulostaa yhtälön ratkaisun

Hyvä:

- Osaat muokata koodia siten, että sillä voi ratkaista myös muita yhtälöitä, esim. $x - \sqrt{x + 4} = 0$
- Ohjelma tulostaa yhtälön ratkaisun ja iteraatioiden lukumäärän

Erinomainen:

- Kaikki edelliset vaatimukset
- Ohjelma piirtää aluksi funktion kuvaajan matplotlib-kirjastolla
- Käyttäjältä kysytään alkuarvaus / aloitusväli kuvan perusteella
- Ohjelma ratkaisee yhtälön
- Tulostetaan ratkaisu ja iteraatioiden lukumäärä
- Lopuksi ohjelma piirtää funktion kuvaajan uudelleen ja ratkaisupiste on merkitty kuvaajaan punaisella rastilla

- Vinkki, Google on sinun kaverisi näissä asioissa. Etsi tietoa myös englanniksi.
- Virallisen matplotlib-kirjaston aloitusopas löytyy [tästä linkistä](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)