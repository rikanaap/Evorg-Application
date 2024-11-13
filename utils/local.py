from src.service.user import User

# Local User
_userDatabase = User().databaseModel
localUser =  _userDatabase.getModel()
def setLocalUser(username):
    global localUser 
    localUser = _userDatabase.checkIdentifier(username)
    if(not localUser): raise ValueError("No Username in User Database")
    return

def getLocalUser(): return localUser

