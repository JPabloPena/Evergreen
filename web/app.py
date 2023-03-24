from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

variables_list_estado = ['Activo','Inactivo']
variables_list_tipo = ['Monitoreo','Control','Detección']
variables_list_lenguaje = ['Python','Java','C#','C++']

@app.route('/listarAplicaciones',methods=['GET'])
def listarAplicaciones():
    aplicaciones_list = requests.get('http://localhost:5001/tipoAplicaciones').json()
    return render_template('listarAplicaciones.html', aplicaciones=aplicaciones_list)

@app.route('/crearAplicacion',methods=['GET'])
def crearAplicacion():
    return render_template('crearAplicacion.html', variables_estado=variables_list_estado, variables_tipo=variables_list_tipo, variables_lenguaje=variables_list_lenguaje)

@app.route('/guardarAplicacion',methods=['POST'])
def guardarAplicacion():
    aplicacion = dict(request.values)
    requests.post('http://localhost:5001/tipoAplicaciones',json=aplicacion)
    return(listarAplicaciones())

app.run(host='0.0.0.0',port=8000)