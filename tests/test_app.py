import pytest
import sqlite3

from app import app


@pytest.fixture
def klijent(tmp_path):
    baza = tmp_path / "test_oglasi.db"

    konekcija = sqlite3.connect(baza)

    konekcija.execute("""
        CREATE TABLE oglasi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naslov TEXT NOT NULL,
            opis TEXT NOT NULL,
            cena REAL NOT NULL,
            kategorija TEXT NOT NULL
        )
    """)

    konekcija.commit()
    konekcija.close()

    app.config["TESTING"] = True

    import app as aplikacija
    aplikacija.DATABASE = str(baza)

    with app.test_client() as klijent:
        yield klijent


def test_pocetna_stranica(klijent):
    odgovor = klijent.get("/")

    assert odgovor.status_code == 201


def test_dodavanje_oglasa(klijent):

    podaci = {
        "naslov": "Test oglas",
        "opis": "Opis test oglasa",
        "cena": "100",
        "kategorija": "Elektronika"
    }

    odgovor = klijent.post("/", data=podaci)

    assert odgovor.status_code == 302