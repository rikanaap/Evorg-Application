from utils.helper import clear, generateTitle, generateRoundown
from utils.local import getLocalEvent, getLocalUser, getLocalEventId
from src.design.update_event import updateEvent
from src.service.user import User

import inquirer
_userService = User()

def detailEvent(callback):
    firstInput = True
    while True:
        clear()
        user = getLocalUser()
        event  = getLocalEvent()
        eventId = getLocalEventId()
        
        generateTitle("Detail Event", 18)
        print(f"Nama Event  : {event['event_name']}")
        print(f"Jadwal      : {event['event_date']} {event['event_time']}")
        print(f"Tempat      : {event['event_location']}, {event['city']}")
        print(f"Deskripsi   : {event['event_desc']}")

        print("")
        choices = ["Assign Event", "Lihat Rundown", "Back"] if user['role'] != "spv" else ["Update Event", "Back"]
        answer = inquirer.list_input("Go to...", choices=choices)
        if not firstInput:
            if answer == "Update Event":
                return updateEvent(lambda: detailEvent(callback))
            elif answer == "Assign Event":
                assignEvent(lambda: detailEvent(callback))
                clear()
                return callback()
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