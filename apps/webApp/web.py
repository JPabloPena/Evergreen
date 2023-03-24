import json
from flask import Flask, jsonify, render_template

with open('../TiposSensor.json') as json_file:
    data = json.load(json_file)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    for p in data:
        print('Referencia: ' + p['referencia'])
        print('Nombre: ' + p['nombre'])
        print('variable: ' + p['variable'])
        print('')
    return jsonify(data)

@app.route('/tiposSensores', methods=['GET'])
def listTiposSensor():
    return render_template('listTiposSensor.html', variable=data)

app.run('0.0.0.0',port=5000,debug=True)
