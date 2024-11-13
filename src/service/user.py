import utils.local as localData
from src.database.database import Database
class User:
    def __init__(self):
        self.databaseModel = Database('user')
        
    def getAll(self):
        return self.databaseModel.getData()
       
    def validateUser(self, username, password):
        data = self.getAll()
        users = data.get("datas", {})
        if username in users:
            user = users[username]
            if user["password"] == password:
                localData.setLocalUser(username)
                return {"success": True, "user": user}
        return {"success": False, "message": "Username atau password salah!"} 
    def assignEvent(self, eventId):
        data = self
