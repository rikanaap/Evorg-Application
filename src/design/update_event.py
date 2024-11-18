from utils.helper import generateTitle, clear
import inquirer
from src.service.event import Event
from src.design.dashboard_spv import dashboard

_eventService = Event()

def redirectToSpvDashboard():
    dashboard()

def updateEvent():
    clear()
    print(generateTitle("Update Event", 14))
    print("\n")

    id_questions = [
        inquirer.Text('id', message="Masukkan ID yang ingin diperbaharui: ")
    ]
    id_answers = inquirer.prompt(id_questions)
    
    id = id_answers['id']
    
    event = _eventService.getEventId(id)
    
    if not event:
        print(f"Event dengan id {id} tidak ditemukan, tekan enter untuk kembali ke menu utama")
        input()
        return
    print(f"Event ditemukan: {event}")
    event['event_name'] = input(f"Nama Event [{event['event_name']}]: ") 
    event['event_date'] = input(f"Tanggal Event [{event['event_date']}]: ") 
    event['event_time'] = input(f"Waktu Event [{event['event_time']}]: ")
    event['city'] = input(f"Kota Event [{event['city']}]: ") 
    event['event_location'] = input(f"Lokasi Event [{event['event_location']}]: ") 
    event['event_desc'] = input(f"Deskripsi Event [{event['event_desc']}]: \n") 
    
    while True:
        confirm = input("Konfirmasi perubahan (yes/no): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Perubahan dibatalkan.")
            return
        
        if _eventService.updateEvent(id, event):
            print("Event berhasil diperbarui.")
            redirectToSpvDashboard()
        else:
            print("Terjadi kesalahan saat memperbarui event.")

