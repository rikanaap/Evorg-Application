from src.service.event import Event
from utils.helper import generateTitle, clear
from src.design.dashboard_spv import dashboard

_eventService = Event()

def redirectToSpvDashboard():
    dashboard()

def createEvent():
    clear()
    print(generateTitle("Dashboard", 14))
    datas = _eventService.databaseModel.DB_MODEL_DATA
    
    datas['event_name'] = input("Nama Event\t\t\t: ")
    datas['event_date'] = input("Tanggal Event (YYYY-MM-DD)\t: ")  
    datas['event_time'] = input("Waktu Event (hh:mm)\t\t: ")
    datas['city'] = input("Kota Event\t\t\t: ")
    datas['event_location'] = input("Lokasi Event\t\t\t: ")
    datas['event_desc'] = input("Deskripsi Event\t\t\t: \n")
    
    while True:
        confirm = input("Konfirmasi (yes/no) : ").strip().lower()
        if confirm in ['yes', 'y']:
            # print(datas)
            print(_eventService.createOne(datas))
            print("data berhasil dikirim")
            redirectToSpvDashboard()
            break
        elif confirm in ['no', 'n']:
            print("data gagal dikirim")
            break
        else:
            print("Invalid input. Please enter yes or no.")
