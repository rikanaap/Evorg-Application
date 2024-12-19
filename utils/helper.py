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
    while True:
        clear()
        if runFC:
          runFC()
        tableRoundown(id)
        time.sleep(0.2)
        if keyboard.is_pressed("esc"):
            break

def requiredInput(message):
   first_time = True
   while True:
      if first_time: print("\033[F\033[K", end="")
      first_time = False
      answer = input(message)
      if answer != "": return answer

def confirmation(key):
  print(f"Tekan apapun untuk melanjutkan, tekan {key} untuk kembali")
  if keyboard.read_event().name == key: return False
  return True