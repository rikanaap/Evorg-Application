from src.service.user import User

# Local User
_userDatabase = User().databaseModel
_localUser =  _userDatabase.getModel()
def setLocalUser(username):
    global _localUser 
    _localUser = _userDatabase.checkIdentifier(username)
    if(not _localUser): raise ValueError("No Username in User Database")
    return

def getLocalUser(): return _localUser
def printLocalUser():
    global _localUser
    print(F"""Username : {_localUser['username']}
Role     : {"Supervisor" if _localUser['role'] != "user" else "User"}
""")