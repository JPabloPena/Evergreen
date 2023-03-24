from model import TipoSensorModel

class TiposSensorListPresenter:

    def __init__(self):
        self.model = TipoSensorModel("../TiposSensor.json")

    def listTiposSensor(self):
        return self.model.readAll()