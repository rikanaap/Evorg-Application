from utils.helper import clear, generateTitle, generateRoundown
from utils.local import getLocalEvent, getLocalUser, getLocalEventId, setLocalRundown
from src.service.user import User
from src.design.table import tableRoundown, tableInputRundown
from src.design.createRundown import createRundown
from src.design.updateRundown import updateRundown

import inquirer, keyboard
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
            while keyboard.is_pressed("enter"): pass
            tableIndex = tableInputRundown(lambda: detailRundown(callback), rundownId, "Pilih posisi rundown akan berada dibawah...")
            while keyboard.is_pressed("enter"): pass
            return createRundown(lambda: detailRundown(callback), tableIndex)
        elif answer == "Edit Rundown":
            while keyboard.is_pressed("enter"): pass
            tableIndex = tableInputRundown(lambda: detailRundown(callback), rundownId, "Pilih rundown yang akan dirubah...")
            while keyboard.is_pressed("enter"): pass
            return updateRundown(lambda: detailRundown(callback), tableIndex)
        elif answer == "Back": 
            clear()
            return callback()
        else: print("Invalid choice. Please choose a valid option.")