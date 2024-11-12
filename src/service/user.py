from src.database.database import Database
class User:
    def __init__(self):
        self.databaseModel = Database('user')
        
    def getAll(self):
        return self.databaseModel.getData()
       
    def validateUser(self, username, password):
        data = self.getAll()
        users = data.get("datas", {})
        # Check username ada di daabase ga
        if username in users:
            user = users[username]
            # Validasi password
            if user["password"] == password:
                return {"success": True, "user": user}
        return {"success": False, "message": "Username atau password salah!"} 
    