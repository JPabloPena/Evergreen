import json

with open('TiposSensor.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print(f'''Referencia: {p['referencia']}\nNombre: {p['nombre']}\nVariable: {p['variable']}\n''')
'''
        print('Referencia: ' + p['referencia'])
        print('Nombre: ' + p['nombre'])
        print('Variable: ' + p['variable'])
        print('')
'''