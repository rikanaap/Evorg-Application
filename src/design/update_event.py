from utils.helper import generateTitle, clear, multilineInput
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
        inquirer.Text('roundown_identifier', message="Masukkan ID yang ingin diperbaharui ")
    ]
    id_answers = inquirer.prompt(id_questions)
    
    roundown_identifier = id_answers['roundown_identifier']
    
    event_id, event = _eventService.getEventByRoundownIdentifier(roundown_identifier)
    
    if not event:
        print(f"Event dengan id {roundown_identifier} tidak ditemukan, tekan enter untuk kembali ke menu utama")
        input()
        return
    print(f"Event ditemukan: {event}")
    event['event_name'] = input(f"Nama Event [{event['event_name']}]\t:  ") 
    event['event_date'] = input(f"Tanggal Event [{event['event_date']}]\t: ") 
    event['event_time'] = input(f"Waktu Event [{event['event_time']}]\t: ")
    event['city'] = input(f"Kota Event [{event['city']}]\t: ") 
    event['event_location'] = input(f"Lokasi Event [{event['event_location']}]\t: ") 
    event['event_desc'] = multilineInput(f"Deskripsi Event [{event['event_desc']}]: \n") 
    
    while True:
        confirm = input("Konfirmasi perubahan (yes/no): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Perubahan dibatalkan.")
            return
        
        if _eventService.getEventByRoundownIdentifier(roundown_identifier, event):
            print("Event berhasil diperbarui.")
            redirectToSpvDashboard()
        else:
            print("Terjadi kesalahan saat memperbarui event.")

