from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "moja-tajna"

DATABASE = "oglasi.db"


def kreiraj_bazu():
    konekcija = sqlite3.connect(DATABASE)

    konekcija.execute("""
        CREATE TABLE IF NOT EXISTS oglasi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naslov TEXT NOT NULL,
            opis TEXT NOT NULL,
            cena REAL NOT NULL,
            kategorija TEXT NOT NULL
        )
    """)

    konekcija.commit()
    konekcija.close()


@app.route("/", methods=["GET", "POST"])
def pocetna():

    if request.method == "POST":

        naslov = request.form["naslov"]
        opis = request.form["opis"]
        cena = request.form["cena"]
        kategorija = request.form["kategorija"]

        konekcija = sqlite3.connect(DATABASE)

        konekcija.execute("""
            INSERT INTO oglasi (naslov, opis, cena, kategorija)
            VALUES (?, ?, ?, ?)
        """, (naslov, opis, cena, kategorija))

        konekcija.commit()
        konekcija.close()

        flash("Oglas je uspešno dodat!", "success")

        return redirect(url_for("pocetna"))

    konekcija = sqlite3.connect(DATABASE)

    oglasi = konekcija.execute("""
        SELECT * FROM oglasi
        ORDER BY id DESC
    """).fetchall()

    konekcija.close()

    return render_template("index.html", oglasi=oglasi)


if __name__ == "__main__":
    kreiraj_bazu()
    app.run(host="0.0.0.0", port=5000)
    # komentar