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
  print(message + ", ketik 'exit' untuk menyelesaikan:")
  
  user_lines = []
  while True:
      line = input()
      if line.lower() == "exit": break
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
