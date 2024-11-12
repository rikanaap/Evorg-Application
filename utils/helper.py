import os

def generateTitle(nama, length):
    return print(f"{'=' * length} {nama} {'=' * length}")

def clear():
  if os.name == 'nt':  # Windows
    os.system("cls")
  else:
    os.system("clear")
