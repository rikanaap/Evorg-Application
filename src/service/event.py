from src.database.database import Database
from src.service.roundown import Roundown
class Event:
    def __init__(self):
        self.databaseModel = Database('event')
        self.serviceRoundown = Roundown()
    
    def getEventId(self, id):
        return self.databaseModel.getData(id)
    
    def updateEvent(self, id, updates):
        return self.databaseModel.updateData(id, updates)

    def getAll(self):
        databaseData = self.databaseModel.getData()
        databaseData = databaseData['datas'].values()
        return databaseData
    
    def createOne(self, data):
        data['roundown_identifier'] = f"{self.databaseModel.getCurrentId() + 1}-RNON"
        return self.databaseModel.addData(data)


