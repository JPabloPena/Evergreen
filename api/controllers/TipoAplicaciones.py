from flask import jsonify, request
from db.db import cnx

class TipoAplicacion():
    #global cur
    #cur = cnx.cursor()

    def list():
        lista = []
        cur = cnx.cursor()
        cur.execute("SELECT * FROM tipo_aplicaciones")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            # Create a zip object from two lists
            registro = zip(columns, row)
            # Create a dictionary from zip object
            json = dict(registro)
            lista.append(json)
        cur.close
        cnx.close
        return jsonify(lista)

    def create(body):
        # Campos
        data = (body['nombre'],body['puerto'],body['estado'],body['tipo'],body['lenguaje'])
        cur = cnx.cursor()
        # Sentencia SQL
        sql = "INSERT INTO tipo_aplicaciones(nombre, puerto, estado, tipo, lenguaje) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        cur.close
        cnx.close
        return {'estado': "Insertado"}, 200
