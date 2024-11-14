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
    
    def assignEvent(self, eventId):
        from utils.local import getLocalUser
        userData = getLocalUser()
        assignedEventSet = list(userData.get('assignedEvent') or [])
        if eventId in assignedEventSet: return userData

        assignedEventSet.append(eventId)
        userData['assignedEvent'] = assignedEventSet
        self.databaseModel.updateData(userData['username'], userData)
        return userData

    
    def createOne(self, data):
      return self.databaseModel.addUser(data)
      
    def cekRegister(self, username):
      if self.databaseModel.checkIdentifier(username):
        return {"success": False, "message": "Username sudah terdaftar."}
      return {"success": True, "message": "Registrasi berhasil."}
    
    def hashPassword(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


