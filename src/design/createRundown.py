from utils.helper import generateTitle, multilineInput, clear, confirmation
from src.design.table import tableRoundown, tableInputRundown
from utils.local import getLocalRundown, getLocalRundownId
from src.service.roundown import Roundown
from src.design.confirm_rundown import confirmRundown
import keyboard
_rundownService = Roundown()

def createRundown(callback, index_below):
    rundownId = getLocalRundownId()
    # rundownData = getLocalRundown()
    clear(), generateTitle('Add New Rundown', 14)
    confirm = confirmation('esc')
    if not confirm: return callback()
    try:
      rundown_name = input("Rundown Name\t: ")
      duration = int(input("Duration (menit): "))
    except ValueError:
      print("Durasi harus berupa angka!")
      return createRundown(callback, index_below)
    description = multilineInput("Description\t: \nTulis deskripsi rundown")

    new_rundown = {
        "roundown_name": rundown_name, 
        "duration": duration, 
        "description": description,
        "index_below": index_below
    }

    def on_create_success():
      _rundownService.createOne(rundownId, new_rundown)
      callback()
        
    def on_create_failure(): return callback()

    confirmRundown("create"
     , on_create_success
     , on_create_failure
     , data=new_rundown)