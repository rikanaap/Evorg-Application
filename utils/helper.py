import os
import keyboard
from colorama import Fore
from tabulate import tabulate

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