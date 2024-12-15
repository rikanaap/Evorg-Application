from utils.helper import generateTitle, multilineInput, clear
from src.design.table import tableRoundown, tableInputRundown
from utils.local import getLocalRundown, getLocalRundownId
from src.service.roundown import Roundown
from src.design.confirm_rundown import confirmRundown


def createRundown(callback, index_below):
    rundownId = getLocalRundownId()
    rundownData = getLocalRundown()

    clear(), generateTitle('Add New Rundown', 14)
    rundown_name = input("Rundown Name\t: ")    
    description = multilineInput("Description\t: ")
    duration = int(input("Duration\t: "))
    index =  tableInputRundown(createRundown, event_data.get("roundown_identifier"))

    # confirmRundown("create"
    # , #TODO: Function when success or confirmation is yes
    # , #TODO: Function when failed or confirmation is no
    # , data={
    #     "roundown_name": rundown_name, 
    #     "duration": duration, 
    #     "description": description, 
    #     "index_below": index_below
    #     })


