from utils.helper import generateTitle, clear
from utils.local import printLocalUser
from src.design.createEvent import createEvent
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
<<<<<<< HEAD
        print("hal create event")
        from src.design.create_event import createEvent
        createEvent.create_event() #hal. create event
=======
        createEvent()
        # createEvent() #hal. create event
>>>>>>> eb818d4137ac532803d4cbd6e0dacc618162ec29
    elif answer == "List All Created Event":
        print("hal created")
        # list_all_created_event() #hal list all created event
    elif answer == "Logout":
        from src.design.first_page import first_page
 


 
        while True:
                confirm = input("Konfirmasi (yes/no): ").lower().strip()
                if confirm in ["yes", "y"]:
                    first_page()
                    break
                elif confirm in ["no", "n"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
 
    else:
        print("Invalid choice. Please choose a valid option.")
        dashboard()







