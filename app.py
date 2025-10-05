from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

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

        
        # ... (código que coleta os dados) ...
        # AQUI usamos 'with' para garantir que o 'conn.close()' seja chamado automaticamente
        with sqlite3.connect("igreja.db", timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO membros (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo ,culto)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo ,culto))
            conn.commit()

        return "<h2>✅ Dados salvos com sucesso!</h2>"
    except Exception as e:
        return f"<h2>❌ Erro ao salvar: {e}</h2>"



   

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False, port=5001)
