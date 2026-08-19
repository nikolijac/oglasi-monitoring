import pytest

from app import app


@pytest.fixture
def klijent():
    app.config["TESTING"] = True

    with app.test_client() as klijent:
        yield klijent


def test_pocetna_stranica(klijent):
    odgovor = klijent.get("/")

    assert odgovor.status_code == 200


def test_dodavanje_oglasa(klijent):

    podaci = {
        "naslov": "Test oglas",
        "opis": "Opis test oglasa",
        "cena": "100",
        "kategorija": "Elektronika"
    }

    odgovor = klijent.post("/", data=podaci)

    assert odgovor.status_code == 302