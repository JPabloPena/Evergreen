from model import TipoSensorModel
from view import TiposSensorListView

class GestionarTiposSensorController:

    def __init__(self):
        self.model = TipoSensorModel("../TiposSensor.json")
        self.view = TiposSensorListView(self.model)

    def listTiposSensor(self):
        self.view.paintTiposSensor()