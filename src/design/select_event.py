from utils.helper import generateTitle, clear
from src.service.event import Event
from src.design.table import tableInputEvent
from utils.local import setLocalEvent, getLocalEvent
_eventService = Event()

def selectEvent():
    clear()
    selectedId = tableInputEvent()
    setLocalEvent(selectedId)
    return print(getLocalEvent()) #Function detail 