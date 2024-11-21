from tabulate import tabulate
from colorama import Fore
from utils.helper import clear
from src.service.event import Event
import keyboard

_eventService = Event()
maxCharLength = 20
def tableEvent():
    eventData = _eventService.getAll() #Ambil data dari service
    tableData = [["Nama Event", "Jadwal", "Tempat", "Deskripsi"]]
    for data in eventData: tableData.append([data['event_name'], f"{data['event_date'] + ' ' + data['event_time']}", f"{data['event_location'] + ', ' + data['city']}", (data['event_desc'] if len(data['event_desc']) <= maxCharLength else data['event_desc'][0:maxCharLength - 2] + "...")]) #Masukin ke tableData (variable yang bakal dipake buat tabulate)
    return print(tabulate(tableData, headers="firstrow", tablefmt="github"))

def tableInputEvent():
  table = list(_eventService.getRawAll()['datas'].items())
  tableLength = len(table)
  if tableLength < 1 or not table[0]: return False
  
  inputIndex, shownTable = 1,[["Nama Event", "Jadwal", "Tempat", "Deskripsi"]]
  for mainKey, data in table:
     shownTable.append([" ", data['event_name'], f"{data['event_date'] + ' ' + data['event_time']}", f"{data['event_location'] + ', ' + data['city']}", (data['event_desc'] if len(data['event_desc']) <= maxCharLength else data['event_desc'][0:maxCharLength - 2] + "...")])
  shownTableLength = len(shownTable)

  while True:
    clear()
    shownTable[inputIndex][0] = Fore.GREEN + '>' + Fore.WHITE
    print(tabulate(shownTable, headers="firstrow", tablefmt="github"))
    
    event = keyboard.read_event()
    if event.event_type == "down":
        if event.name == "down": 
            shownTable[inputIndex][0] = " "
            inputIndex = (inputIndex + 1) % shownTableLength if (inputIndex + 1 != 0) else 1
            if inputIndex == 0: inputIndex = 1
        elif event.name == "up": 
            shownTable[inputIndex][0] = " "
            inputIndex = (inputIndex - 1) % shownTableLength
            if inputIndex == 0: inputIndex = 1
        elif event.name == "enter":
           return table[inputIndex - 1][0]
        else: continue
