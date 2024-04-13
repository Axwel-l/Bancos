from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def pagina_consulta():
    return render_template('index.html')

@app.route('/api/', methods=['GET'])
def consultar_bancos():
    codigo = request.args.get('codigo')
    if codigo:
        banco = consultar_banco(codigo)
        if banco:
            return jsonify(banco)
        else:
            return jsonify({'message': 'Banco não encontrado'}), 404
    else:
        return listar_bancos()

def listar_bancos():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bancos')
    bancos = cursor.fetchall()
    conn.close()
    return jsonify(bancos)

def consultar_banco(codigo):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bancos WHERE codigo_compensaçao = ?', (codigo,))
    banco = cursor.fetchone()
    conn.close()
    return banco

if __name__ == '__main__':
    app.run(debug=True)