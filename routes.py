from flask import render_template, request # type: ignore
import sqlite3

from main import app

#mudei alguma coisa

@app.route('/')
def home():
    cadeiras = {
        "APII": 0,
        "Lógica matemática": 0,
        "Matemática discreta": 0,
        "Libras": 0,
        "ADM": 0,
        "Método científico": 0
    }

    conn = sqlite3.connect("meu_banco.db")
    cursor = conn.cursor()

    cursor.execute("SELECT cadeira FROM faltas")
    search_db = cursor.fetchall()
    
    conn.close()

    for s in search_db:
        match s[0]:
            case "Lógica matemática":
                cadeiras["Lógica matemática"] += 1
            case "Matemática discreta":
                cadeiras["Matemática discreta"] += 1
            case "APII":
                cadeiras["APII"] += 1
            case "Libras":
                cadeiras["Libras"] += 1
            case "Método científico":
                cadeiras["Método científico"] += 1
            case "ADM":
                cadeiras["ADM"] += 1

    return render_template("index.html", cadeiras=cadeiras)

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/submit-date', methods=['POST'])
def submit_date():
    cadeira = request.form.get('cadeira')
    data = request.form.get('dia-falta')

    conn = sqlite3.connect("meu_banco.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO faltas(cadeira, dia) VALUES(?, ?);", (cadeira, data))
    conn.commit()

    conn.close()

    return f"Você faltou em {cadeira} na data {data}, preparese para se foder no final do semestre"


