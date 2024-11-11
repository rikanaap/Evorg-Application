from src.database.database import Database
class Event:
    def __init__(self):
        self.databaseModel = Database('event')
    def getAll(self):
        return self.databaseModel.getData()