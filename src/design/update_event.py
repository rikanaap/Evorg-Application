from utils.helper import generateTitle, clear, multilineInput
import inquirer
from src.service.event import Event
from src.design.dashboard_spv import dashboard
from utils.local import setLocalEvent, getLocalEvent, getLocalUser, getLocalEventId
from colorama import Fore
_eventService = Event()

def redirectToSpvDashboard():
    dashboard()

def updateEvent(callback):
    clear()
    generateTitle("Update Event", 14) 
    event_id = getLocalEventId()
    event = _eventService.getEventId(event_id)
    if not event :
        print(f"Event dengan id {event_id} tidak ditemukan, tekan enter untuk kembali ke menu utama"), input()
        return
    event_questions = [
        inquirer.Text('event_name', message=f"Nama Event [{event['event_name']}]\t", default=event['event_name']),
        inquirer.Text('event_date', message=f"Tanggal Event [{event['event_date']}]\t", default=event['event_date']),
        inquirer.Text('event_time', message=f"Waktu Event [{event['event_time']}]\t", default=event['event_time']),
        inquirer.Text('city', message=f"Kota Event [{event['city']}]\t\t", default=event['city']),
        inquirer.Text('event_location', message=f"Lokasi Event [{event['event_location']}]\t", default=event['event_location']),
        inquirer.Text('event_desc', message=f"Deskripsi Event [{event['event_desc']}]\t", default=event['event_desc']),
    ]
    answers = inquirer.prompt(event_questions)

    while True:
        clear()
        print(
f"""Tolong Periksa apakah data sudah benar, data dibawah akan ditampilkan dan dilihat oleh user:\n
{Fore.GREEN}Nama Event\t: {Fore.WHITE + answers['event_name']}
{Fore.GREEN}Tanggal & Waktu\t: {Fore.WHITE + answers['event_date'] + " " + answers['event_time']}
{Fore.GREEN}Lokasi\t\t: { Fore.WHITE + answers['city'] + ", " + answers['event_location']}

{Fore.GREEN}Deskripsi:
{Fore.WHITE + answers['event_desc']}""")
              
        confirm = input("Konfirmasi perubahan (yes/no): ").strip().lower()
        if confirm not in ['y', 'yes']:
            callback()
            return
        
        if _eventService.updateEvent(event_id, answers):
            print("Event berhasil diperbarui.")
            redirectToSpvDashboard()
        else:
            print("Terjadi kesalahan saat memperbarui event.")

