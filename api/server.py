from flask import Flask, request
from flask_cors import CORS
from controllers.TipoAplicaciones import TipoAplicacion

app = Flask(__name__)
CORS(app)

@app.route('/tipoAplicaciones',methods=['GET'])
def getAll():
    return (TipoAplicacion.list())

@app.route('/tipoAplicaciones',methods=['POST'])
def postOne():
    body = request.json
    return (TipoAplicacion.create(body))

app.run(host='0.0.0.0',port=5001)