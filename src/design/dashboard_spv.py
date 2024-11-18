from utils.helper import generateTitle, clear
from utils.local import printLocalUser
from src.design.createEvent import createEvent
import inquirer
# from src.design.logout import logout

def dashboard():
    clear()
    generateTitle("Dashboard SPV", 14)
    print("Welcome to the SPV's dashboard!!")
    printLocalUser()
    
    answer = inquirer.list_input("Go to...", choices=["Create New", "List All Created Event", "Logout"])
    
    if answer == "Create New":
        createEvent()
        # createEvent() #hal. create event
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







