from utils.helper import generateTitle, clear, logOut
from utils.local import printLocalUser
import inquirer
from src.design.createdPage import display_event_list

def dashboard():
    clear()
    generateTitle("Dashboard SPV", 14)
    print("Welcome to the SPV's dashboard!!")
    printLocalUser()
    
    answer = inquirer.list_input("Go to...", choices=["Create New", "List All Created Event", "Logout"])
    
    if answer == "Create New":
        print("hal create event")
        from src.design.create_event import createEvent
        createEvent(dashboard) #hal. create event
    elif answer == "List All Created Event":
        return display_event_list()
 
    elif answer == "Logout": return logOut(callback=dashboard)
    else:
        print("Invalid choice. Please choose a valid option.")
        dashboard()







