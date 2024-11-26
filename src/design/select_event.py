from utils.helper import generateTitle, clear
from src.service.event import Event
from src.service.user import User
from src.design.table import tableInputEvent
from utils.local import setLocalEvent, getLocalEvent, getLocalUser, getLocalEventId
import inquirer, time

_userService = User()
_eventService = Event()

def selectEvent(callback=None):
    clear()
    selectedId = tableInputEvent(callback)  
    setLocalEvent(selectedId)
    detailEvent()
    action(callback)
    
def detailEvent():
    clear()
    event = getLocalEvent() 
    
    if not event:
        print("Tidak ada event yang dipilih.")
        return

    print(generateTitle("Detail Event", 18))
    print(f"Nama Event  : {event['event_name']}")
    print(f"Jadwal      : {event['event_date']} {event['event_time']}")
    print(f"Tempat      : {event['event_location']}, {event['city']}")
    print(f"Deskripsi   : {event['event_desc']}")
    
def action(callback=None):
    detailEvent()
    eventId = getLocalEventId()
    user = getLocalUser()  
    assignedEventIds = user.get('assignedEvent', [])
    isAssigned = eventId in assignedEventIds
    
    choices = ["Lihat rundown", "Back"]
    
    if not isAssigned:
        choices.insert(1, "Assign event")  
        
    answer = inquirer.list_input(
        "Go to...", choices=choices)

    if answer == "Assign event":
        assignEvent(callback)
    elif answer == "Back":
        selectEvent(callback)

def assignEvent(callback=None):
    clear()
    event = getLocalEvent()
    
    while True:
        confirm = input("Apakah Anda ingin bergabung dengan event ini? (yes/no): ").strip().lower()
        
        if confirm in ["yes", "y"]:
            key = getLocalEventId()
            if key:
                updatedUser = _userService.assignEvent(key)
                if key in updatedUser['assignedEvent']:
                    print(f"Berhasil bergabung dengan event '{event['event_name']}'!")
                    time.sleep(3)
                    action(callback)
                    break
                else:
                    print("Gagal bergabung dengan event. Silakan coba lagi.")
            else:
                print("Tidak ada event yang dipilih.")
                break
        elif confirm in ["no", "n"]:
            print("Anda memilih untuk tidak bergabung dengan event ini.")
            action(callback)  
            break
        else:
            print("Input tidak valid. Silakan coba lagi.")
  