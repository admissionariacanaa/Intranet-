from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

# Configuração MySQL usando variáveis de ambiente do Render
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_DATABASE_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('DB_NAME')
app.config['MYSQL_DATABASE_PORT'] = int(os.environ.get('DB_PORT', 3306))

mysql = MySQL()
mysql.init_app(app)

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

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO membros (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo, culto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome, grupo, sexo, data_nascimento, telefone, endereco, bairro, cep, membro, batizado, cargo, culto))

        conn.commit()
        cursor.close()
        conn.close()

        return "<h2>✅ Dados salvos com sucesso!</h2>"
    except Exception as e:
        return f"<h2>❌ Erro ao salvar: {e}</h2>"

# Ajuste para rodar localmente ou no Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=port)
