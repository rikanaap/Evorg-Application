from utils.helper import generateTitle, addDuration, maxCharacter, clear, requiredInput
from utils.local import getLocalRundown, getLocalRundownId, getLocalEvent
from src.service.roundown import Roundown
from tabulate import tabulate
from colorama import Fore
from datetime import datetime

_roundownService = Roundown()

def confirmRundown(ident, positive_cb, negative_cb, data):

    clear()
    generateTitle("Confirmation Create Event", 18)
    roundownData = getLocalRundown()
    eventData = getLocalEvent()
    eventTime = datetime.strptime(eventData.get('event_time'), "%H:%M").time()


    if ident == "create" : roundownData.insert(data["index_below"] + 1, data)
    if ident == "update" : roundownData[data['index_below']] = data

    tableData = [["Nama Kegiatan", "Jadwal", "Deskripsi"]]
    for rundownData in roundownData:
        rdDuration = rundownData["duration"]
        previousEventTime = eventTime
        eventTime = addDuration(eventTime, rdDuration)

        tableData.append([rundownData['roundown_name'],  f"{previousEventTime} - {eventTime} ({rdDuration})", maxCharacter(rundownData['description'].split('\n')[0], 20)])

    print(tabulate(tableData, headers="firstrow", tablefmt="github"))
    print()

    print(f"{Fore.GREEN}Nama Rundown{Fore.WHITE}\t: {data['roundown_name']}")
    print(f"{Fore.GREEN}Duration{Fore.WHITE}\t: {data['duration']}")
    print(f"{Fore.GREEN}Deskripsi{Fore.WHITE}\t:\n{data['description']}")

    while True:
        answer = requiredInput("Konfirmasi untuk membuat data? (yes/no) : ")
        if answer == "yes" or answer == "y": return positive_cb()
        elif answer == "no" or answer == "n": return negative_cb()