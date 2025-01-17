from utils.helper import generateTitle, clear, generateRoundown
from src.service.event import Event
from src.service.user import User
from src.design.table import tableInputEvent
from utils.local import setLocalEvent, getLocalEvent, getLocalUser, getLocalEventId
import inquirer, time
from src.design.createdPage import display_event_list

_userService = User()
_eventService = Event()

def selectEvent(backCallback, nextCallback, assigned=None, created=None):
    clear()
    selectedId = tableInputEvent(backCallback, assigned, created )  
    print(selectedId)
    setLocalEvent(str(selectedId))
    nextCallback()
  
# def showRundown(callback=None):
#   clear()
#   generateTitle("Rundown Event", 18)
#   eventId = getLocalEventId()
#   generateRoundown(eventId)
#   answer = inquirer.list_input(
#         "Go to...", choices=["Back"])
#   if answer == "Back":
#     action(callback)