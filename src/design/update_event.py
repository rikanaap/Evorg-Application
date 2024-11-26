from utils.helper import generateTitle, clear, multilineInput
import inquirer
from src.service.event import Event
from src.design.dashboard_spv import dashboard
from utils.local import setLocalEvent, getLocalEvent, getLocalUser, getLocalEventId

_eventService = Event()

def redirectToSpvDashboard():
    dashboard()

def updateEvent():
    clear()
    print(generateTitle("Update Event", 14))
    print("\n")
 
    event_id = getLocalEventId()
    print(f"Trying to update event with ID: {event_id}")
    event = _eventService.getEventId(event_id)
    if not event :
        print(f"Event dengan id {event_id} tidak ditemukan, tekan enter untuk kembali ke menu utama")
        input()
        return
    event_questions = [
        inquirer.Text('event_name', message=f"Nama Event [{event['event_name']}]", default=event['event_name']),
        inquirer.Text('event_date', message=f"Tanggal Event [{event['event_date']}]", default=event['event_date']),
        inquirer.Text('event_time', message=f"Waktu Event [{event['event_time']}]", default=event['event_time']),
        inquirer.Text('event_location', message=f"Lokasi Event [{event['event_location']}]", default=event['event_location']),
        inquirer.Text('city', message=f"Kota Event [{event['city']}]", default=event['city']),
        inquirer.Text('event_desc', message=f"Deskripsi Event [{event['event_desc']}]", default=event['event_desc']),
    ]
    answers = inquirer.prompt(event_questions)

    while True:
        confirm = input("Konfirmasi perubahan (yes/no): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Perubahan dibatalkan.")
            return
        
        if _eventService.updateEvent(event_id, answers):
            print("Event berhasil diperbarui.")
            redirectToSpvDashboard()
        else:
            print("Terjadi kesalahan saat memperbarui event.")

