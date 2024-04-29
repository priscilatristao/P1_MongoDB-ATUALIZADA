from flask import Flask, request , redirect, url_for,  render_template

import pymongo 

app = Flask(__name__)

connection = pymongo.connector.connect (
    host = 'http://127.0.0.1:3000/',
    user = 'root',
    password = '12345678',
    database = 'mongodb+srv://prilimarj:<12345678>@cluster0.ylej0qf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
)

db_cursor = connection.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/novo_nome', methods=['POST'])
def novo_nome():
    if request.method == 'POST':
        novo_nome_nome = request.form['nome']
        query = 'INSERT INTO novo (nome) VALUES (%s)'
        db_cursor.execute(query, (novo_nome,))
        connection.commit()
    return redirect(url_for('home'))

@app.route('/novo_email', methods=['POST'])
def novo_email():
    if request.method == 'POST':
        nome_email = request.form['nome_email']
        query = 'INSERT INTO cargos (nome) VALUES (%s)'
        db_cursor.execute(query, (nome_email,))
        connection.commit()
    return redirect(url_for('home'))

@app.route('/novo_cadastro', methods=['POST'])
def processar_novo_cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    

    db_cursor.execute(
        'INSERT INTO cadastro (nome, email, senha) VALUES (%s, %s, %s)',
        (nome, email, senha)
    )
    connection.commit()

    return f'Novo cadastro criado: {nome} {email}, senha {senha}'

if __name__ == '__main__':
    app.run(debug=True)