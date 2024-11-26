from utils.helper import generateTitle, clear
from src.service.event import Event
from src.service.user import User
from src.design.table import tableInputEvent
from utils.local import setLocalEvent, getLocalEvent, getLocalUser
import inquirer, time

_eventService = Event()
_userService = User()

def selectAssignedEvent(callback=None):
    clear()
    user = getLocalUser()
    selectedId = tableInputEvent(selectAssignedEvent, assigned=user['assignedEvent'])
    setLocalEvent(selectedId)
    detailEvent()
    action(callback)

def detailEvent():
    clear()
    event = getLocalEvent()
    
    generateTitle("Detail Event", 18)
    print(f"Nama Event  : {event['event_name']}")
    print(f"Jadwal      : {event['event_date']} {event['event_time']}")
    print(f"Tempat      : {event['event_location']}, {event['city']}")
    print(f"Deskripsi   : {event['event_desc']}")

def action(callback=None):
    detailEvent()
    
    choices = ["Lihat rundown", "Back"]
        
    answer = inquirer.list_input(
        "Go to...", choices=choices)

    if answer == "Back":
      selectAssignedEvent(callback)