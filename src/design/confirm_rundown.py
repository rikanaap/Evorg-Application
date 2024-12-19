from utils.helper import generateTitle, addDuration, maxCharacter, clear, requiredInput
from utils.local import getLocalRundown, getLocalRundownId
from src.service.roundown import Roundown
from tabulate import tabulate
from colorama import Fore

_roundownService = Roundown()

def confirmRundown(ident, positive_cb, negative_cb, data):

    clear()
    generateTitle("Confirmation Create Event", 18)
    roundownData = getLocalRundown()

    if ident == "create" : roundownData.insert(data["index_below"] + 1, data)
    #TODO: When the identifier is "update" change the data in index_below
    tableData = [["Nama Kegiatan", "Jadwal", "Deskripsi"]]
    for rundownData in roundownData:
        rdDuration = rundownData["duration"]
        tableData.append([rundownData['roundown_name'],  rdDuration, maxCharacter(rundownData['description'].split('\n')[0], 20)])

    print(tabulate(tableData, headers="firstrow", tablefmt="github"))
    print()

    print(f"{Fore.GREEN}Nama Rundown{Fore.WHITE}\t:{data['roundown_name']}")
    print(f"{Fore.GREEN}Duration{Fore.WHITE}\t: {data['duration']}")
    print(f"{Fore.GREEN}Deskripsi{Fore.WHITE}\t:\n {data['description']}")

    while True:
        answer = requiredInput("Konfirmasi untuk membuat data? (yes/no) : ")

        if answer == "yes" or answer == "y": return positive_cb()
        elif answer == "no" == "n": return negative_cb()