from utils.helper import generateTitle, multilineInput, clear,requiredInput
from src.design.table import tableRoundown, tableInputRundown
from utils.local import getLocalRundown, getLocalRundownId
from src.service.roundown import Roundown
from src.design.confirm_rundown import confirmRundown
import inquirer
_rundownService = Roundown()

def updateRundown(callback, index_below):
    rundownId = getLocalRundownId()
    rundownData = getLocalRundown()
    data_old = rundownData[index_below]


    clear(), generateTitle('Add New Rundown', 14)
    rundown_questions = [
            inquirer.Text('roundown_name', message=f"Nama Rundown [{data_old['roundown_name']}]\t", default=data_old['roundown_name']),
            inquirer.Text('duration', message=f"Durasi Rundown [{data_old['duration']}]\t", default=data_old['duration']),
    ]
    answers = inquirer.prompt(rundown_questions)
    description = multilineInput(f"Deskripsi Rundown\t: \n[{data_old['description']}]\nTulis deskripsi rundown")

    new_rundown = { **answers, "description": description, "index_below": index_below }
    def on_create_success():
      result = _rundownService.updateData(rundownId, new_rundown)
      if result:
        print("Rundown berhasil dibuat!")
      else:
        print("Gagal membuat rundown.")
        
    def on_create_failure():
      print("Rundown gagal dibuat.")

    confirmRundown("create"
     , on_create_success()
     , on_create_failure
     , data=new_rundown)
    