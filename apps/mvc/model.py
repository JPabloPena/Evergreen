import json

class TipoSensorModel:

    def __init__(self,fileName):
        self.fileName = fileName
        with open(self.fileName) as json_file:
            self.data = json.load(json_file)
    
    def readAll(self):
        return self.data