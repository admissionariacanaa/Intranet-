from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Configuração do PostgreSQL (idealmente você colocará isso nas variáveis de ambiente do Render)
DB_HOST = os.getenv("DB_HOST", "dpg-abc123-p1234.render.com")
DB_NAME = os.getenv("DB_NAME", "igreja_db")
DB_USER = os.getenv("DB_USER", "igreja_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "sua_senha_aqui")
DB_PORT = os.getenv("DB_PORT", "5432")

def conectar():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

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

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO membros (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo, culto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo, culto))

        conn.commit()
        cursor.close()
        conn.close()

        return "<h2>✅ Dados salvos com sucesso no PostgreSQL!</h2>"

    except Exception as e:
        return f"<h2>❌ Erro ao salvar: {e}</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


