from tabulate import tabulate
from src.service.event import Event

_eventService = Event()
maxCharLength = 20
def tableEvent():
    eventData = _eventService.getAll() #Ambil data dari service
    tableData = [["Nama Event", "Jadwal", "Tempat", "Deskripsi"]]
    for data in eventData: tableData.append([data['event_name'], f"{data['event_date'] + ' ' + data['event_time']}", f"{data['event_location'] + ', ' + data['city']}", (data['event_desc'] if len(data['event_desc']) <= maxCharLength else data['event_desc'][0:maxCharLength - 2] + "...")]) #Masukin ke tableData (variable yang bakal dipake buat tabulate)
    print(tabulate(tableData, headers="firstrow", tablefmt="github"))