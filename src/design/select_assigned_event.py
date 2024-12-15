from utils.helper import generateTitle, clear, generateRoundown
from src.service.event import Event
from src.service.user import User
from src.design.table import tableInputEvent
from src.design.detail_event import detailEvent
from utils.local import setLocalEvent, getLocalEvent, getLocalUser, getLocalEventId
import inquirer, time

_eventService = Event()
_userService = User()

def selectAssignedEvent():
    from src.design.dashboard_user import dashboard
    clear()
    user = getLocalUser()
    selectedId = tableInputEvent(dashboard, assigned=user['assignedEvent'])
    setLocalEvent(selectedId)
    detailEvent(selectAssignedEvent, { "hide_assigned": True})
    