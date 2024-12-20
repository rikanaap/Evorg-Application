from utils.helper import generateTitle, multilineInput, clear, requiredInput, confirmation
from src.design.table import tableRoundown, tableInputRundown
from utils.local import getLocalRundown, getLocalRundownId, setLocalRundown
from src.service.roundown import Roundown
from src.design.confirm_rundown import confirmRundown
import inquirer
_rundownService = Roundown()

def updateRundown(callback, index_below):
    rundownId = getLocalRundownId()
    setLocalRundown(rundownId)
    rundownData = getLocalRundown()
    data_old = rundownData[index_below]

    clear(), generateTitle('Add New Rundown', 14)
    confirm = confirmation('esc')
    if not confirm: return callback()
    # while keyboard.is_pressed("enter"): pass

    print(rundownData)
    try:
      data_old['roundown_name'] = inquirer.text(message=f"Nama Rundown [{data_old['roundown_name']}]\t", autocomplete=data_old['roundown_name'])
      data_old['duration'] = int(inquirer.text(message=f"Durasi Rundown [{data_old['duration']}]\t"))
    except ValueError: return updateRundown(callback, index_below)

    data_old['description'] = multilineInput(f"Deskripsi Rundown\t[{data_old['description']}]:\nTulis deskripsi rundown")
    data_old['index_below'] = index_below
  
    def on_create_success():
      result = _rundownService.updateData(rundownId, data_old)
      callback()

    def on_create_failure():
      callback()

    confirmRundown("update"
     , on_create_success
     , on_create_failure
     , data=data_old)