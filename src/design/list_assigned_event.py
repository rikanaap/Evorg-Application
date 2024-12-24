from utils.helper import generateTitle, clear
import src.design.table as tableTemplate 
from utils.local import getLocalUser
import inquirer
from src.design.select_assigned_event import selectAssignedEvent

def listAllAssignedEvent():
    from src.design.dashboard_user import dashboard
    
    user = getLocalUser()
    assignedEventIds = user.get('assignedEvent', [])
    searchData = None
    while True:
        clear()
        generateTitle("List All Assigned Events", 33)
        
        choices = ["Search Event","Back to dashboard"]
        
        if not assignedEventIds: print("\n\t\tTidak ada event yang telah di-assign untuk pengguna ini.")
        if assignedEventIds:
            tableTemplate.tableAssignedEvent(assigned=user['assignedEvent'], search=searchData) 
            choices.insert(0, "Select Event")  
        print()
        answer = inquirer.list_input(
            "Next Action...", choices=choices)
        
        if answer == "Back to dashboard": return dashboard()
        elif answer == "Search Event":
            searchData = input("Cari nama event: ")
            continue
        elif answer == "Select Event": return selectAssignedEvent()