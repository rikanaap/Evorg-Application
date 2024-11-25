from utils.helper import generateTitle, clear, logOut
from utils.local import printLocalUser
import inquirer
# from src.design.create_event import createEvent
# from src.design.logout import logout

def dashboard():
    clear()
    generateTitle("Dashboard SPV", 14)
    print("Welcome to the SPV's dashboard!!")
    printLocalUser()
    
    answer = inquirer.list_input("Go to...", choices=["Create New", "List All Created Event", "Logout"])
    
    if answer == "Create New":
        print("hal create event")
        from src.design.create_event import createEvent
        createEvent() #hal. create event
    elif answer == "List All Created Event":
        print("hal created")
        # list_all_created_event() #hal list all created event
    elif answer == "Logout": return logOut()
    else:
        print("Invalid choice. Please choose a valid option.")
        dashboard()







