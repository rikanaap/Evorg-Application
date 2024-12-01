from src.database.database import Database
import hashlib

class User:
    def __init__(self):
        self.databaseModel = Database('user')
        
    def getAll(self):
        return self.databaseModel.getData()
       
    def validateUser(self, username, password):
        from utils.local import setLocalUser
        data = self.getAll()
        users = data.get("datas", {})
        if username in users:
            user = users[username]
            if user["password"] == password:
                setLocalUser(username)
                return {"success": True, "user": user}
        return {"success": False, "message": "Username atau password salah!"} 
    
    def addEvent(self, eventId, identifier="assign"):
        from utils.local import getLocalUser
        userData = getLocalUser()
        identifierDb = "assignedEvent" if identifier == "assign" else "createdEvent"
        tempSet = list(userData.get(identifierDb) or [])
        if eventId in tempSet: return userData

        tempSet.append(eventId)
        userData[identifierDb] = tempSet
        self.databaseModel.updateData(userData['username'], userData)
        return userData

    
    def createOne(self, data):
      return self.databaseModel.addData(data, data['username'])
      
    def cekRegister(self, username):
      if self.databaseModel.checkIdentifier(username):
        return {"success": False, "message": "Username sudah terdaftar."}
      return {"success": True, "message": "Registrasi berhasil."}
    
    def hashPassword(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


