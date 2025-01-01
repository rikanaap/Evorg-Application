from src.service.event import Event
from colorama import Fore
from utils.helper import generateTitle, clear, multilineInput, confirmation, requiredInput, timeInput, dateInput
import keyboard

_eventService = Event()

def createEvent(callback):
    from src.design.dashboard_spv import dashboard

    datas = _eventService.databaseModel.DB_MODEL_DATA
    
    eventCreated = False
    while not eventCreated:
        clear(), generateTitle("Create Event", 14)
        confirm = confirmation('esc', 'q')
        if not confirm: return callback()

        datas['event_name'] = requiredInput(f"Nama Event\t\t\t: ")
        datas['event_date'] = dateInput(f"Tanggal Event (YYYY-MM-DD)\t: ")
        datas['event_time'] = timeInput(f"Waktu Mulai Event (HH:MM)\t: ")
        datas['city'] = requiredInput(f"Dilaksanakan di Kota\t\t: ")
        datas['event_location'] = requiredInput(f"Detail Lokasi Event\t\t: ")
        datas['event_desc'] = multilineInput("Ketik deskripsi event")

        clear()
        print(
f"""Tolong Periksa apakah data sudah benar, data dibawah akan ditampilkan dan dilihat oleh user:\n
{Fore.GREEN}Nama Event\t: {Fore.WHITE + datas['event_name']}
{Fore.GREEN}Tanggal & Waktu\t: {Fore.WHITE + datas['event_date'] + " " + datas['event_time']}
{Fore.GREEN}Lokasi\t\t: { Fore.WHITE + datas['city'] + ", " + datas['event_location']}

{Fore.GREEN}Deskripsi:
{Fore.WHITE + datas['event_desc']}""")
        while True:
            confirm = input("\nKonfirmasi untuk membuat data? (yes/no) : ").strip().lower()
            if confirm in ['yes', 'y']:
                _eventService.createOne(datas)
                callback()
                eventCreated = True
                break
            else:
                secondConfirm = input("Lanjut membuat data? (yes/no) : ").strip().lower()
                if secondConfirm in ['yes', 'y']: break
                else:
                    callback()
                    eventCreated = True
                    break