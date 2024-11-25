from src.service.user import User
from src.service.event import Event
from utils.global_db import GlobalDatabase

# Local User
_userDatabase = User().databaseModel
_eventDatabase = Event().databaseModel
_globalDatabase = GlobalDatabase()
_localUser =  _userDatabase.getModel()
_localEventId = 0
_localEvent = _eventDatabase.getModel()

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

def setLocalEvent(id):
    global _localEventId
    global _localEvent

    _localEventId = id
    _localEvent = _eventDatabase.checkIdentifier(id)
    return

def getLocalEvent(): return _localEvent

def getLocalEventId(): return _localEventId

def checkOneTimeLogin():
    globalData = _globalDatabase.getData()
    isLogged = globalData.get("oneTimeLogin")
    if not isLogged: return False

    setLocalUser(globalData.get("user_username"))
    return _localUser

def emptyUserData():
    global _localUser 
    _localUser =  _userDatabase.getModel()
    _globalDatabase.clearData()
    return True
