from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("patients.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            disease TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db()
    patients = conn.execute(
        "SELECT * FROM patients"
    ).fetchall()
    conn.close()

    return render_template("index.html", patients=patients)


@app.route("/add", methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        disease = request.form["disease"]

        conn = get_db()

        conn.execute("""
            INSERT INTO patients
            (name, age, gender, phone, disease)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, gender, phone, disease))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_patient.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_patient(id):

    conn = get_db()

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        disease = request.form["disease"]

        conn.execute("""
            UPDATE patients
            SET name=?, age=?, gender=?, phone=?, disease=?
            WHERE id=?
        """, (name, age, gender, phone, disease, id))

        conn.commit()
        conn.close()

        return redirect("/")

    patient = conn.execute(
        "SELECT * FROM patients WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit_patient.html",
        patient=patient
    )


@app.route("/delete/<int:id>")
def delete_patient(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM patients WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)