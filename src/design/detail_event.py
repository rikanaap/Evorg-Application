from utils.helper import clear, generateTitle, generateRoundown, eventTimeValid
from utils.local import getLocalEvent, getLocalUser, getLocalEventId
from src.design.update_event import updateEvent
from src.design.detail_rundown import detailRundown
from src.design.select_rundown import selectRundown
from src.service.user import User
from colorama import Fore
import inquirer
_userService = User()

def detailEvent(callback, filter={"hide_assigned": False }, shouldRecurse=False):
    if shouldRecurse: return callback()
    removeAssignEvent = filter.get('hide_assigned')
    firstInput = True
    while True:
        clear()
        user = getLocalUser()
        event  = getLocalEvent()
        eventId = getLocalEventId()
        if eventId is None: return callback()
        timeValid = eventTimeValid(event.get('event_time'))
        
        generateTitle("Detail Event", 18)
        print(f"Nama Event  : {event['event_name']}")
        print(f"Jadwal      : {event['event_date']} {event['event_time']}")
        print(f"Tempat      : {event['event_location']}, {event['city']}")
        print(f"Deskripsi   : {event['event_desc']}")

        print("")
        if user['role'] != 'user' and not timeValid: print(Fore.RED + "Please change event time!" + Fore.WHITE)
        choices = ["Assign Event", "Back"] if user['role'] != "spv" else ["Update Event", "Back"]
        if timeValid: choices.insert(1, "Lihat Rundown") if user['role'] != "spv" else choices.insert(1, 'Detail Rundown')
        if user['role'] != "spv" and removeAssignEvent: choices.pop(0)
        answer = inquirer.list_input("Go to...", choices=choices)
        if not firstInput:
            if answer == "Update Event":
                return updateEvent(lambda: detailEvent(callback, shouldRecurse=True))
            elif answer == "Assign Event":
                assignEvent(lambda: detailEvent(callback, shouldRecurse=True))
                clear()
                return callback()
            elif answer == "Detail Rundown":
                return detailRundown(lambda: detailEvent(callback, shouldRecurse=True))
            elif answer == "Lihat Rundown":
                generateRoundown(str(eventId), lambda: print("Press 'esc' to go back\n"))
            elif answer == "Back": 
                clear()
                return callback()
            else: print("Invalid choice. Please choose a valid option.")
        else: firstInput = False

def assignEvent(callback=None):
    user = getLocalUser()
    clear()
    event  = getLocalEvent()
    eventId  = getLocalEventId()

    generateTitle("Assign Event", 18)
    print(f"Nama Event  : {event['event_name']}")
    print(f"Jadwal      : {event['event_date']} {event['event_time']}")
    print(f"Tempat      : {event['event_location']}, {event['city']}")
    print(f"Deskripsi   : {event['event_desc']}")

    while True:
        confirm = input("Apakah Anda ingin bergabung dengan event ini? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]: _userService.addEvent(eventId)
        return callback()