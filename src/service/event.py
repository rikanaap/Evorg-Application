from src.database.database import Database
from src.service.roundown import Roundown
from src.service.user import User
class Event:
    def __init__(self):
        self.databaseModel = Database('event')
        self.serviceRoundown = Roundown()
        self.serviceUser = User()
    
    def getEventId(self, roundown_identifier):
        return self.databaseModel.checkIdentifier(roundown_identifier)
    
    def getAll(self, assigned_array=None, created_array=None, search=None):
        from utils.helper import searchKey
        databaseData = self.databaseModel.getData(assigned=assigned_array, created=created_array)
        databaseData = databaseData['datas'].values()
        if search: databaseData = searchKey(databaseData, search, keys=['event_name', 'event_date', 'event_time', 'event_location', 'city'])
        return databaseData
    
    def getRawAll(self, assigned_array=None, created_array=None ):
        return self.databaseModel.getData(assigned=assigned_array, created=created_array)
    
    def getOne(self, id):
        return self.databaseModel.checkIdentifier(id)
    
    def createOne(self, data):
        data['roundown_identifier'] = f"{self.databaseModel.getCurrentId() + 1}-RNON"
        self.serviceRoundown.createOne(data['roundown_identifier'], None)
        self.serviceUser.addEvent(str(self.databaseModel.getCurrentId() + 1), "create")
        return self.databaseModel.addData(data)
    
    def updateEvent(self, event_id, updates):
        return self.databaseModel.updateData(event_id, updates)