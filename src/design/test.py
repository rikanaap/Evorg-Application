from src.service.roundown import Roundown
from src.service.event import Event
from tabulate import tabulate
import inquirer

_roundownService = Roundown()
_eventService = Event()

def getAll():
    roundownData = _roundownService.getAll() #Ambil data dari service
    tableData = []
    for data in roundownData: #Loop data dari service
        for dataList in data:
            tableData.append([dataList['roundown_name'], dataList['duration'], dataList['description']]) #Masukin ke tableData (variable yang bakal dipake buat tabulate)
    print(tabulate(tableData))

def queryTest():
    print('Test query')
    inquirer.list_input("Pilih mas", choices=['Opsi 1', 'Opsi 2', 'Opsi 3'])

def createEVent():
    datas = _eventService.databaseModel.DB_MODEL_DATA
    datas['event_name'] = input("Nama Event\t: ")
    datas['event_time'] = input("Waktu Event\t: ")
    datas['event_date'] = input("Tanggal Event\t:")
    datas['event_desc'] = input("Deskripsi Event\t: \n")
    datas['city'] = input("Kota Event\t: ")
    datas['event_location'] = input("Lokasi Event\t: ")

    print(_eventService.createOne(datas))