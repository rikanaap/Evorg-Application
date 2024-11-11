from src.database.database import Database
class Roundown:
    def __init__(self):
        self.databaseModel = Database('roundown')
    def getAll(self):
        return self.databaseModel.getData()