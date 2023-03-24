import json
import sys

accion  = sys.argv[1]

if accion == 'listTiposSensor':
    with open('TiposSensor.json') as json_file:
        data = json.load(json_file)
    for p in data:
        print('Referencia: ' + p['referencia'])
        print('Nombre: ' + p['nombre'])
        print('Variable: ' + p['variable'])
        print('')
elif accion == 'readTipoSensor':
    with open('TiposSensor.json') as json_file:
        data = json.load(json_file)
    for p in data:
        if p['referencia'] == sys.argv[2]:
            print('Referencia: ' + p['referencia'])
            print('Nombre: ' + p['nombre'])
            print('Variable: ' + p['variable'])
            print('')
elif accion == 'createTipoSensor':
    pass
elif accion == 'updateTipoSensor':
    pass
elif accion == 'deleteTipoSensor':
    pass
elif accion == 'createParcela':
    pass
    '''
    Y asi con todas las entidades de dominio.
    '''
else :
    print('Accion no considerada')