from utils.helper import generateTitle, multilineInput, clear, requiredInput, confirmation, intInput, alertMessage
from src.design.table import tableRoundown, tableInputRundown
from utils.local import getLocalRundown, getLocalRundownId, setLocalRundown
from src.service.roundown import Roundown
from src.design.confirm_rundown import confirmRundown
import inquirer, keyboard
from colorama import Fore
_rundownService = Roundown()

def updateRundown(callback, index_below):
    rundownId = getLocalRundownId()
    setLocalRundown(rundownId)
    rundownData = getLocalRundown()
    data_old = rundownData[index_below]

    clear(), generateTitle('Update Rundown', 14)
    confirm = confirmation('esc')
    if not confirm: return callback()

    data_old['roundown_name'] = requiredInput(f"Nama Rundown [{data_old['roundown_name']}]\t: ")
    data_old['duration'] = intInput(f"Durasi Rundown [{data_old['duration']}]\t: ")
    data_old['description'] = multilineInput(f'''
{Fore.GREEN}Deskripsi sebelumnya: {Fore.WHITE}
{data_old['description']}
{Fore.GREEN}Deskripsi baru{Fore.WHITE}''')
    data_old['index_below'] = index_below
  
    def on_create_success():
      result = _rundownService.updateData(rundownId, data_old)
      alertMessage(f"{result[index_below]['roundown_name']} Berhasil di update", callback )

    confirmRundown("update"
     , on_create_success
     , callback
     , data=data_old)