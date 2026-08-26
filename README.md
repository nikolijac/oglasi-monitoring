\# Oglasi Monitoring – CI/CD i automatizovani feedback loop



\## 1. Opis projekta



Oglasi Monitoring je jednostavna web aplikacija razvijena u Python-u korišćenjem Flask framework-a i SQLite baze podataka.



Aplikacija omogućava korisniku da unese novi oglas koji sadrži:



\- naslov

\- opis

\- cenu

\- kategoriju



Nakon uspešnog unosa korisniku se prikazuje povratna poruka da je oglas uspešno dodat.



Pored same aplikacije, projekat implementira automatizovani CI/CD pipeline pomoću GitHub Actions-a. Pipeline automatski proverava aplikaciju, izvršava testove, prikuplja osnovne sistemske metrike i šalje rezultat izvršavanja na Discord.



Cilj projekta je demonstracija automatizovanog feedback loop-a u DevOps okruženju.



\---



\## 2. Tehnologije



Projekat koristi sledeće tehnologije:



\- Python 3.13

\- Flask

\- SQLite

\- pytest

\- Git

\- GitHub

\- GitHub Actions

\- Discord Webhook



\---



\## 3. Funkcionalnosti aplikacije



Aplikacija omogućava:



\- unos novog oglasa

\- čuvanje oglasa u SQLite bazi

\- prikaz postojećih oglasa

\- prikaz poruke nakon uspešnog dodavanja oglasa



Primer uspešne poruke:



> Oglas je uspešno dodat!



\---



\## 4. CI/CD pipeline



GitHub Actions workflow se automatski pokreće nakon svakog `push` događaja na `main` granu.



Pipeline izvršava sledeće korake:



1\. Preuzima projekat sa GitHub-a.

2\. Podešava Python okruženje.

3\. Instalira potrebne zavisnosti.

4\. Proverava sintaksu aplikacije.

5\. Pokreće automatske testove pomoću pytest-a.

6\. Prikuplja sistemske metrike.

7\. Šalje rezultat na Discord.



Workflow se nalazi u:



```text

.github/workflows/deploy.yml

