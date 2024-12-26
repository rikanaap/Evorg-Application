from utils.helper import generateTitle, clear, multilineInput, confirmation, requiredInput, timeInput, dateInput
import inquirer, keyboard
from src.service.event import Event
from src.design.dashboard_spv import dashboard
from utils.local import setLocalEvent, getLocalEvent, getLocalUser, getLocalEventId
from colorama import Fore
_eventService = Event()

def redirectToSpvDashboard():
    dashboard()

def updateEvent(callback):
    event_id = getLocalEventId()
    event = _eventService.getEventId(event_id)
    if not event :
        print(f"Event dengan id {event_id} tidak ditemukan, tekan enter untuk kembali ke menu utama"), input()
        return

    itemUpdated = False
    while not itemUpdated:
        clear(),generateTitle("Update Event", 14) 
        confirm = confirmation('esc')
        if not confirm: return callback()
        
        keyboard.unblock_key('enter')
        answers = {}
        answers['event_name'] = requiredInput(f"Nama Event [{event['event_name']}]\t\t: ")
        answers['event_date'] = dateInput(f"Tanggal Event [{event['event_date']}]\t: ")
        answers['event_time'] = timeInput(f"Waktu Mulai Event [{event['event_time']}]\t: ")
        answers['city'] = requiredInput(f"Dilaksanakan di Kota [{event['city']}]\t: ")
        answers['event_location'] = requiredInput(f"Detail Lokasi Event [{event['event_location']}]\t: ")
        answers['event_desc'] = multilineInput(f'''
{Fore.GREEN}Deskripsi sebelumnya:{Fore.WHITE}
{event['event_desc']}
{Fore.GREEN}Deskripsi baru:{Fore.WHITE}''')

        while True:
            clear()
            print(
f"""Tolong Periksa apakah data sudah benar, data dibawah akan ditampilkan dan dilihat oleh user:\n
{Fore.GREEN}Nama Event\t: {Fore.WHITE + answers['event_name']}
{Fore.GREEN}Tanggal & Waktu\t: {Fore.WHITE + answers['event_date'] + " " + answers['event_time']}
{Fore.GREEN}Lokasi\t\t: { Fore.WHITE + answers['city'] + ", " + answers['event_location']}

{Fore.GREEN}Deskripsi:
{Fore.WHITE + answers['event_desc']}""")
                
            confirm = input("Konfirmasi untuk perubahan data? (yes/no): ").strip().lower()
            if confirm in ['y', 'yes']:
                if _eventService.updateEvent(event_id, answers):
                    print("Event berhasil diperbarui.")
                    return callback()
            else:
                secondConfirm = input("Lanjut membuat data? (yes/no): ").strip().lower()
                if secondConfirm in ['y', 'yes']: break
                else:
                    return callback()