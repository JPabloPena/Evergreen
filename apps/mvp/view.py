from presenter import TiposSensorListPresenter

class TiposSensorListView:

    def __init__(self):
        self.presenter = TiposSensorListPresenter()
    
    def paintTiposSensor(self):
        for p in self.presenter.listTiposSensor():
            print('Name: ' + p['referencia'])
            print('Website: ' + p['nombre'])
            print('From: ' + p['variable'])
            print('')
