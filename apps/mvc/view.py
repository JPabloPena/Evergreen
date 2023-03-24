class TiposSensorListView:

    def __init__(self,model):
        self.model = model
    
    def paintTiposSensor(self):
        for p in self.model.readAll():
            print('Referencia: ' + p['referencia'])
            print('Nombre: ' + p['nombre'])
            print('Variable: ' + p['variable'])
            print('')
