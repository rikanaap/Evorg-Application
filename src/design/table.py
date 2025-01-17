from tabulate import tabulate
from colorama import Fore
from utils.helper import clear, addDuration, maxCharacter
from src.service.event import Event
from src.service.roundown import Roundown
from datetime import datetime
import keyboard, time

_eventService = Event() 
_roundownService = Roundown()
maxCharLength = 20

def tableEvent(assigned=None, created=None, search=None):
    eventData = _eventService.getAll(assigned_array=assigned, created_array=created, search=search) #Ambil data dari service
    tableData = [["Nama Event", "Jadwal", "Tempat", "Deskripsi"]]
    for data in eventData: tableData.append([data['event_name'], f"{data['event_date'] + ' ' + data['event_time']}", f"{data['event_location'] + ', ' + data['city']}", maxCharacter(data['event_desc'], maxCharLength).split('\n')[0]]) #Masukin ke tableData (variable yang bakal dipake buat tabulate)
    return print(tabulate(tableData, headers="firstrow", tablefmt="github"))

def tableCreatedEvent(created=None, search=None):
   eventData = _eventService.getAll(created_array=created, search=search) #Ambil data dari service
   tableData = [["Nama Event", "Jadwal", "Tempat", "Deskripsi"]]
   for data in eventData: tableData.append([data['event_name'], f"{data['event_date'] + ' ' + data['event_time']}", f"{data['event_location'] + ', ' + data['city']}", maxCharacter(data['event_desc'], maxCharLength).split('\n')[0]]) #Masukin ke tableData (variable yang bakal dipake buat tabulate)
   return print(tabulate(tableData, headers="firstrow", tablefmt="github")) 

def tableAssignedEvent(assigned=None, search=None):
   eventData = _eventService.getAll(assigned_array=assigned, search=search) #Ambil data dari service
   tableData = [["Nama Event", "Jadwal", "Tempat", "Deskripsi"]]
   for data in eventData: tableData.append([data['event_name'], f"{data['event_date'] + ' ' + data['event_time']}", f"{data['event_location'] + ', ' + data['city']}", maxCharacter(data['event_desc'], maxCharLength).split('\n')[0]]) #Masukin ke tableData (variable yang bakal dipake buat tabulate)
   return print(tabulate(tableData, headers="firstrow", tablefmt="github"))

def tableRoundown(event_id, highlightTime=None):
    eventData = _eventService.getOne(event_id)
    roundownData = list(_roundownService.getOne(eventData.get("roundown_identifier")) or [])

    currentTime = datetime.now().time()
    eventTime = datetime.strptime(eventData.get('event_time'), "%H:%M").time()
    tableData = [["Nama Kegiatan", "Jadwal", "Deskripsi"]]
    if highlightTime: tableData[0].append("X")
    if roundownData and roundownData:
     for data in roundownData:
        rdDuration = data["duration"]
        previousEventTime = eventTime
        eventTime = addDuration(eventTime, rdDuration)

        isCurrent = previousEventTime <= currentTime <= eventTime if highlightTime else None
        rundownItem = [data['roundown_name'], f"{previousEventTime} - {eventTime} ({rdDuration}`)", maxCharacter(data['description'], maxCharLength).split('\n')[0]]
        if highlightTime: rundownItem.append(f"{Fore.GREEN}<{Fore.WHITE}" if isCurrent else "")
        tableData.append(rundownItem)
     return print(tabulate(tableData, headers="firstrow", tablefmt="github"))
    else:
      print("Tidak ada data rundown")

def tableInputEvent(callback, assigned=None, created=None):
    table = list(_eventService.getRawAll(assigned_array=assigned, created_array=created)['datas'].items())
    tableLength = len(table)
    if tableLength < 1 or not table[0]: return False
    
    inputIndex, shownTable = 1,[["Nama Event", "Jadwal", "Tempat", "Deskripsi"]]
    for mainKey, data in table:
        shownTable.append([" ", data['event_name'], f"{data['event_date'] + ' ' + data['event_time']}", f"{data['event_location'] + ', ' + data['city']}", maxCharacter(data['event_desc'], maxCharLength).split('\n')[0]])
    shownTableLength = len(shownTable)
    while True:
        clear()
        print("Use"+ Fore.GREEN + " esc " + Fore.WHITE + "button to go back")

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
            elif event.name == "esc":
                clear()
                return callback()
            else: continue

def tableInputRundown(callback, rd_id, notes="Please select rundown"):
  table = list(_roundownService.getOne(rd_id) or []) 
  tableLength = len(table)
  if tableLength < 1 or not table[0]: return 0
  
  inputIndex, shownTable = 1,[["Pilih","Nama Kegiatan", "Jadwal", "Deskripsi"]]
  for data in table:
      shownTable.append([" ",data['roundown_name'],data['duration'], maxCharacter(data['description'], maxCharLength).split('\n')[0]])
  shownTableLength = len(shownTable)

  while True:
    clear()
    print("Use"+ Fore.GREEN + " esc " + Fore.WHITE + "button to go back")
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
           return inputIndex - 1
        elif event.name == "esc":
            clear()
            return callback()
        else: continue