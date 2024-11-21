from src.service.user import User
from src.service.event import Event

# Local User
_userDatabase = User().databaseModel
_eventDatabase = Event().databaseModel
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