from utils.helper import clear, generateTitle, generateRoundown
from utils.local import getLocalEvent, getLocalUser, getLocalEventId, setLocalRundown
from src.service.user import User
from src.design.table import tableRoundown, tableInputRundown
from src.design.createRundown import createRundown
from src.design.updateRundown import updateRundown

import inquirer
_userService = User()

def detailRundown(callback):
    from src.design.detail_event import detailEvent
    while True:
        clear()
        user = getLocalUser()
        event  = getLocalEvent()
        eventId = getLocalEventId()
        rundownId = event.get('roundown_identifier')

        generateTitle("Detail Rundown", 18)
        tableRoundown(eventId)
        setLocalRundown(rundownId)
        print("")

        choices = ["Tambah Rundown", "Edit Rundown", "Back"]
        # if event.get(''):
        answer = inquirer.list_input("Go to...", choices=choices)
        if answer == "Tambah Rundown":
            tableIndex = tableInputRundown(lambda: detailRundown(callback), rundownId, "Pilih posisi rundown akan berada dibawah...")
            return createRundown(callback, tableIndex)
        elif answer == "Edit Rundown":
            tableIndex = tableInputRundown(lambda: detailRundown(callback), rundownId, "Pilih rundown yang akan dirubah...")
            return updateRundown(callback, tableIndex)
        elif answer == "Back": 
            clear()
            return callback()
        else: print("Invalid choice. Please choose a valid option.")
