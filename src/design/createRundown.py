from utils.helper import generateTitle, multilineInput, clear
from src.design.table import tableRoundown, tableInputRundown
from utils.local import getLocalRundown, getLocalRundownId
from src.service.roundown import Roundown
from src.design.confirm_rundown import confirmRundown

_rundownService = Roundown()

def createRundown(callback, index_below):
    rundownId = getLocalRundownId()
    rundownData = getLocalRundown()

    clear(), generateTitle('Add New Rundown', 14)
    rundown_name = input("Rundown Name\t: ")    
    description = input("Description\t: ")
    try:
      duration = int(input("Duration (menit)\t: "))
    except ValueError:
      print("Durasi harus berupa angka!")
      return callback()
    index_below =  tableInputRundown(createRundown, rundownId)

    new_rundown = {
        "roundown_name": rundown_name, 
        "duration": duration, 
        "description": description,
        "index_below": index_below
    }

    def on_create_success():
      _rundownService.createOne(rundownId, new_rundown)
      callback()
        
    def on_create_failure():
       callback()

    confirmRundown("create"
     , on_create_success
     , on_create_failure
     , data=new_rundown)