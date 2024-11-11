from src.database.database import Database
class User:
    def __init__(self):
        self.databaseModel = Database('user')
    def getAll(self):
        return self.databaseModel.getData()