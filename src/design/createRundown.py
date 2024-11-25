from utils.helper import generateTitle, multilineInput
from src.design.table import tableRoundown, tableInputRundown
from utils.local import getLocalEventId, getLocalEvent, setLocalEvent
from src.service.roundown import Roundown


def createRundown():
   
    event_id = getLocalEventId()
    setLocalEvent(str(event_id))
    event_data = getLocalEvent()
    print(event_data)
    generateTitle('Create rundown', 14)
    tableRoundown(str(event_id))
    rundown_name = input("Rundown Name\t: ")    
    description = multilineInput("Description\t: ")
    duration = int(input("Duration\t: "))
    index =  tableInputRundown(createRundown, event_data.get("roundown_identifier"))
    confirm = input("Confirm (yes/no)\t: ")



