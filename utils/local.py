from src.service.user import User

# Local User
userDatabase = User().databaseModel
localUser =  userDatabase.getModel()
def setLocalUser(username):
    global localUser 
    localUser = userDatabase.checkIdentifier(username)
    if(not localUser): raise ValueError("No Username in User Database")
    return

def getLocalUser(): return localUser

