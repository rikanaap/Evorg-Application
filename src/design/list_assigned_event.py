from utils.helper import generateTitle, clear
from src.design.select_event import selectEvent
import src.design.table as tableTemplate 
import inquirer

def listAllAssignedEvent():
    from src.design.dashboard_user import dashboard

    clear(), generateTitle("List All Assigned Event", 33), print()
    tableTemplate.tableAssignedEvent() 
    answer = inquirer.list_input("Next Action...", choices=["Select Event", "Back to Dashboard"])
    if answer == "Back to Dashboard": return dashboard()
    elif answer == "Select Event": return selectEvent(listAllAssignedEvent)
