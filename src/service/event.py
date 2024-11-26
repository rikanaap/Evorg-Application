from src.database.database import Database
from src.service.roundown import Roundown
class Event:
    def __init__(self):
        self.databaseModel = Database('event')
        self.serviceRoundown = Roundown()
    
    def getEventId(self, roundown_identifier):
        return self.databaseModel.checkIdentifier(roundown_identifier)
    
    def getAll(self, assigned_array=[], created_array=[]):
        databaseData = self.databaseModel.getData(assigned=assigned_array, created=created_array)
        databaseData = databaseData['datas'].values()
        return databaseData
    
    def getRawAll(self, assigned_array=[], created_array=[] ):
        return self.databaseModel.getData(assigned=assigned_array, created=created_array)
    
    def getOne(self, id):
        return self.databaseModel.checkIdentifier(id)
    
    def createOne(self, data):
        data['roundown_identifier'] = f"{self.databaseModel.getCurrentId() + 1}-RNON"
        return self.databaseModel.addData(data)
    
    def getEventByRoundownIdentifier(self, roundown_identifier):
        all_events = self.databaseModel.getData().get('datas', {})
        for event_id, event_data in all_events.items():
            if event_data.get('roundown_identifier') == roundown_identifier:
                return event_id, event_data 
        return None, None
    
    def updateEvent(self, roundown_identifier, updates):
        event_id, event = self.getEventByRundownIdentifier(roundown_identifier)
        if not event:
            return False 
        return self.updateEvent(event_id, updates)
    
