from utils.helper import generateTitle, clear
from src.service.event import Event
from src.design.table import tableInputEvent
from utils.local import setLocalEvent, getLocalEvent
_eventService = Event()

def selectEvent():
    clear()
    selectedId = tableInputEvent()
    setLocalEvent(selectedId)
    return detailEvent()
    
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