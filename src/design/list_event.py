from utils.helper import generateTitle, clear
import src.design.table as tableTemplate 
import inquirer

def listAllEvent():
    from src.design.dashboard_user import dashboard

    clear(), generateTitle("List All Event", 38), print()
    tableTemplate.tableEvent(), print()
    answer = inquirer.list_input("Next Action...", choices=["Select Event", "Back to Dashboard"])
    if answer != "Assign Event": return dashboard()
    # Assign event
