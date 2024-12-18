from utils.helper import generateTitle, addDuration, maxCharacter, clear, requiredInput
from utils.local import getLocalRundown, getLocalRundownId
from src.service.roundown import Roundown
from tabulate import tabulate
from colorama import Fore

_roundownService = Roundown()

def confirmRundown(ident, positive_cb, negative_cb, data):

    # clear()
    generateTitle("Confirmation Create Event", 18)
    roundownData = getLocalRundown()

    if ident == "create" : roundownData.insert(data["index_below"], data)
    #TODO: When the identifier is "update" change the data in index_below
    tableData = [["Nama Kegiatan", "Jadwal", "Deskripsi"]]
    for data in roundownData:
        rdDuration = data["duration"]
        tableData.append([data['roundown_name'],  ({rdDuration}), maxCharacter(data['description'], 20)])

    print(tabulate(tableData, headers="firstrow", tablefmt="github"))
    print()

    print(f"{Fore.GREEN}Nama Rundown{Fore.WHITE}\t:{data['roundown_name']}")
    print(f"{Fore.GREEN}Duration{Fore.WHITE}\t: {data['duration']}")
    print(f"{Fore.GREEN}Deskripsi{Fore.WHITE}\t:\n {data['description']}")

    answer = requiredInput("Konfirmasi untuk membuat data? (yes/no) : ")

    if answer == "yes" or answer == "y":
        positive_cb()
    else:
        negative_cb()

