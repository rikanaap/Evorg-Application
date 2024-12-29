import os, keyboard, time
from colorama import Fore
from tabulate import tabulate
from datetime import datetime, timedelta
from utils.local import emptyUserData

def generateTitle(nama, length):
    return print(f"{'=' * length} {nama} {'=' * length}")

def clear():
  if os.name == 'nt': os.system("cls")
  else: os.system("clear")

def multilineInput(message):
  print(message + ", tekan 'ctrl' + 'enter untuk menyelesaikan:")
  
  user_lines = [] 
  while True:
      if keyboard.is_pressed('ctrl') and keyboard.is_pressed('enter'): break
      line = input()
      # if line.lower() == "exit": break
      # if line.strip() == "": continue
      user_lines.append(line)
  return "\n".join(user_lines)

def addDuration(refTime, duration):
  time_object = refTime
  if isinstance(refTime, str): time_object = datetime.strptime(refTime, "%H:%M").time()
  datetime_object = datetime.combine(datetime.min, time_object)
  updated_datetime = datetime_object + timedelta(minutes=duration)
  refTime = updated_datetime.time()
  return refTime

def maxCharacter(str, max):
   return str if len(str) <= max else str[0 : max - 2] + "..."

def logOut(callback=None):
  from src.design.first_page import first_page
  while True:
      confirm = input("Konfirmasi (yes/no): ").lower().strip()
      if confirm in ["yes", "y"]:
        emptyUserData()
        first_page()
        break
      elif confirm in ["no", "n"]:
        if callback:
          callback()
        break
      else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def generateRoundown(id, runFC=None):
    from src.design.table import tableRoundown
    from src.service.event import Event
    _eventService = Event()
    while True:
        eventStartTime = _eventService.getOne(id)['event_time']
        clear()
        if runFC:
          runFC()
        print(f'''{Fore.GREEN}Jam Sekarang : {Fore.WHITE}{str(datetime.now().time()).split(".")[0]}
{Fore.GREEN}Event Dimulai: {Fore.WHITE}{eventStartTime}
''')
        tableRoundown(id, highlightTime=True)
        time.sleep(0.2)
        if keyboard.is_pressed("esc"):
            break

def requiredInput(message, ignoreFirst=False):
   while True:
      if not ignoreFirst:
        answer = input(message)
        if answer != "": return answer
      ignoreFirst = False
      print("\033[F\033[K", end="")

def intInput(message):
  while True:
    try:
        answer = int(input(message))
        return answer
    except ValueError: print("\033[F\033[K", end="")

def timeInput(message):
  while True:
    try:
        answer = input(message) 
        datetime.strptime(answer, "%H:%M").time()
        return answer
    except ValueError: print("\033[F\033[K", end="")

def confirmation(cancelKey='esc', nextKey='q'):
  print(f"Tekan {nextKey} untuk melanjutkan, tekan {cancelKey} untuk kembali")
  keyboard.block_key('enter')
  while True:
    if keyboard.is_pressed(cancelKey): return False
    if keyboard.is_pressed(nextKey): return True

def eventTimeValid(event_time):
  try:
    datetime.strptime(event_time, "%H:%M").time()
    return True
  except:
    return False 
  
def searchKey(array_data,key, value):
  filteredData = []
  for data in array_data:
    dataKey = data.get(key)
    if not dataKey: continue
    if str(value).lower() in str(dataKey).lower(): filteredData.append(data)
  return filteredData
def alertMessage(message, callback):
  clear()
  length = len(message)
  print("=" * length)
  print(message)
  print("=" * length)
  time.sleep(3)
  return callback()