from utils.helper import generateTitle, clear, logOut
from utils.local import printLocalUser
from src.design.list_event import listAllEvent
from src.design.list_assigned_event import listAllAssignedEvent
import inquirer

def dashboard():
    clear()
    generateTitle("Dashboard User", 14)
    print("Welcome to the user's dashboard!!")
    printLocalUser()

    answer = inquirer.list_input("Go to...", choices=["List All Assigned Event", "List All Event", "Logout"])
    
    if answer == "List All Assigned Event": return listAllAssignedEvent()
    elif answer == "List All Event": return listAllEvent()
    elif answer == "Logout": return logOut()
 
    else:
        print("Invalid choice. Please choose a valid option.")
        dashboard()


 

