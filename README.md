# Oglasi Monitoring - CI/CD i automatizovani feedback loop

## 1. Opis projekta

Oglasi Monitoring je jednostavna web aplikacija razvijena u Python-u korišćenjem Flask framework-a i SQLite baze podataka.

Aplikacija omogućava korisniku da unese novi oglas koji sadrži:

* naslov
* opis
* cenu
* kategoriju

Nakon uspešnog unosa korisniku se prikazuje povratna poruka da je oglas uspešno dodat.

Pored same aplikacije, projekat implementira automatizovani CI/CD pipeline pomoću GitHub Actions-a. Pipeline automatski proverava aplikaciju, izvršava testove, prikuplja osnovne sistemske metrike, vrši deployment aplikacije na virtuelnu mašinu pomoću Docker-a i šalje rezultat izvršavanja na Discord.

Cilj projekta je demonstracija automatizovanog feedback loop-a u DevOps okruženju, gde se promena koda automatski proverava, aplikacija se nakon uspešnog testiranja deploy-uje, a rezultat celog procesa se prosleđuje korisniku.

---

## 2. Tehnologije

Projekat koristi sledeće tehnologije:

* Python 3.13
* Flask
* SQLite
* pytest
* Git
* GitHub
* GitHub Actions
* Docker
* Discord Webhook
* Virtuelna mašina

---

## 3. Funkcionalnosti aplikacije

Aplikacija omogućava:

* unos novog oglasa
* čuvanje oglasa u SQLite bazi
* prikaz postojećih oglasa
* prikaz poruke nakon uspešnog dodavanja oglasa

Primer uspešne poruke:

> Oglas je uspešno dodat!

---

## 4. CI/CD pipeline

GitHub Actions workflow se automatski pokreće nakon svakog `push` događaja na `main` granu.

Pipeline je podeljen na CI i CD deo.

CI deo proverava da li je aplikacija ispravna pre deployment-a. U okviru njega se instaliraju potrebne zavisnosti, proverava se Python sintaksa, pokreću se automatski testovi pomoću pytest-a i prikupljaju se osnovne sistemske metrike.

Nakon uspešnog CI procesa pokreće se CD deo. On omogućava automatski deployment nove verzije aplikacije na virtuelnu mašinu pomoću Docker-a.

Na kraju pipeline-a rezultat izvršavanja se šalje na Discord, čime se omogućava automatizovani feedback.

Workflow fajlovi se nalaze u:

```text
.github/workflows/
```

---

## 5. Continuous Integration

CI deo pipeline-a obezbeđuje automatsku proveru aplikacije nakon svake izmene koda.

U okviru CI procesa izvršavaju se sledeći koraci:

1. Preuzimanje projekta sa GitHub-a.
2. Podešavanje Python okruženja.
3. Instalacija potrebnih zavisnosti.
4. Provera sintakse aplikacije.
5. Pokretanje testova pomoću pytest-a.
6. Prikupljanje rezultata testiranja.
7. Pokretanje monitoring skripte.
8. Slanje rezultata na Discord.

Na ovaj način se greške mogu otkriti pre nego što se nova verzija aplikacije deploy-uje.

---

## 6. Monitoring

Za monitoring se koristi fajl `monitoring.py`.

Skripta prikuplja osnovne sistemske metrike i rezultat monitoringa prosleđuje GitHub Actions pipeline-u.

Monitoring je uključen u CI proces kako bi se, pored provere samog koda, dobile i osnovne informacije o sistemu na kojem se pipeline izvršava.

---

## 7. Continuous Deployment

CD deo projekta omogućava automatsko postavljanje nove verzije aplikacije na virtuelnu mašinu nakon uspešnog CI procesa.

Deployment se izvršava pomoću Docker-a. GitHub Actions runner povezan sa virtuelnom mašinom izvršava potrebne Docker komande i pokreće novu verziju aplikacije.

Proces deployment-a obuhvata zaustavljanje i uklanjanje prethodnog containera, kreiranje novog Docker image-a i pokretanje novog containera.

Na ovaj način nije potrebno ručno pokretati aplikaciju nakon svake promene koda.

---

## 8. Docker

Aplikacija se pakuje u Docker image pomoću `Dockerfile` fajla.

Docker image se kreira komandom:

```bash
docker build -t oglasi-app .
```

Nakon kreiranja image-a aplikacija se pokreće u Docker containeru:

```bash
docker run -d --name oglasi-container -p 5000:5000 oglasi-app
```

Container koristi port `5000`, preko kojeg je aplikacija dostupna na virtuelnoj mašini.

Prilikom automatskog deployment-a prethodni container se zaustavlja i uklanja, nakon čega se kreira novi image i pokreće nova verzija containera.

---

## 9. Discord feedback

Za slanje informacija o izvršavanju pipeline-a koristi se Discord Webhook.

Nakon izvršavanja CI/CD procesa, na Discord se šalje informacija o rezultatu pipeline-a.

Na ovaj način korisnik dobija povratnu informaciju o tome da li je proces uspešno završen i da li je deployment izvršen.

Webhook URL se čuva kao GitHub Secret i nije direktno upisan u izvorni kod.

---

## 10. Automatizovani feedback loop

Celokupan proces projekta može se predstaviti kao:

```text
Promena koda -> git push -> GitHub Actions -> CI – testiranje i monitoring -> CD – Docker deployment -> Aplikacija na virtuelnoj mašini -> Discord obaveštenje -> Feedback
```

Na ovaj način projekat povezuje razvoj, testiranje, monitoring, deployment i povratnu informaciju u jedan automatizovan proces.

---

## 11. Pokretanje aplikacije

Za lokalno pokretanje aplikacije potrebno je instalirati dependencies iz `requirements.txt` fajla:

```bash
pip install -r requirements.txt
```

Aplikacija se zatim može pokrenuti komandom:

```bash
python main.py
```

Nakon pokretanja, aplikacija je dostupna na:

```text
http://localhost:5000
```

Testovi se mogu pokrenuti pomoću:

```bash
python -m pytest -q
```

---

## 12. Struktura projekta

Osnovna struktura projekta je:

`app.py` sadrži glavnu Flask aplikaciju i rad sa SQLite bazom, `main.py` služi za pokretanje aplikacije, `monitoring.py` se koristi za prikupljanje sistemskih metrika, dok se testovi nalaze u direktorijumu `tests`.

Docker konfiguracija nalazi se u `Dockerfile` fajlu, a GitHub Actions workflow-i nalaze se u `.github/workflows` direktorijumu.

---

## 13. Rezultat

Projekat omogućava automatizovan tok od izmene i slanja koda na GitHub, preko testiranja i monitoringa, do deployment-a aplikacije na virtuelnu mašinu.

Nakon uspešnog deployment-a nova verzija aplikacije se pokreće u Docker containeru, dok se rezultat procesa prosleđuje na Discord.

Na taj način projekat demonstrira primenu CI/CD principa, Docker kontejnerizacije, monitoringa i automatizovanog feedback loop-a.
