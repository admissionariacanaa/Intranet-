from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Caminho do banco existente
DB_PATH = os.path.join(os.path.dirname(__file__), "igreja.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    try:
        nome = request.form["nome"]
        grupo = request.form["grupo"]
        sexo = request.form["sexo"]
        data_nascimento = request.form["data_nascimento"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]
        bairro = request.form["bairro"]
        cep = request.form["cep"]
        membro = request.form["membro"]
        batizado = request.form["batizado"]
        cargo = request.form["cargo"]
        culto = request.form["culto"]

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO membros (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo, culto)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo, culto))

        conn.commit()
        conn.close()

        return "<h2>✅ Dados salvos com sucesso!</h2>"
    except Exception as e:
        return f"<h2>❌ Erro ao salvar: {e}</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
