from utils.helper import generateTitle, clear
from src.design.select_event import selectEvent
import src.design.table as tableTemplate 
import inquirer
from utils.local import getLocalUser

def listAllEvent():
    from src.design.dashboard_user import dashboard
    user = getLocalUser()
    clear(), generateTitle("List All Event", 38), print()
    tableTemplate.tableEvent() 
    answer = inquirer.list_input("Next Action...", choices=["Select Event", "Back to Dashboard"])
    if answer == "Back to Dashboard": return dashboard()
    elif answer == "Select Event": return selectEvent(listAllEvent)
    # Assign event