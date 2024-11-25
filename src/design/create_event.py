from src.service.event import Event
from colorama import Fore
from utils.helper import generateTitle, clear, multilineInput

_eventService = Event()

def createEvent():
    from src.design.dashboard_spv import dashboard

    clear(), generateTitle("Create Event", 14)
    datas = _eventService.databaseModel.DB_MODEL_DATA
    
    eventCreated = False
    while not eventCreated:
        datas['event_name'] = input("Nama Event\t\t\t: ")
        datas['event_date'] = input("Tanggal Event (YYYY-MM-DD)\t: ")  
        datas['event_time'] = input("Waktu Event (hh:mm)\t\t: ")
        datas['city'] = input("Kota Event\t\t\t: ")
        datas['event_location'] = input("Lokasi Event\t\t\t: ")
        datas['event_desc'] = multilineInput("Tulis deskripsi event")

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
                print("data berhasil dikirim")
                dashboard()
                eventCreated = True
                break
            elif confirm in ['no', 'n']: 
                clear()
                break
