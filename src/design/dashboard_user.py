from utils.helper import generateTitle, clear
from utils.local import printLocalUser
from src.design.list_event import listAllEvent
import inquirer

def dashboard():
    clear()
    generateTitle("Dashboard User", 14)
    print("Welcome to the user's dashboard!!")
    printLocalUser()

    answer = inquirer.list_input("Go to...", choices=["List All Assigned Event", "List All Event", "Logout"])
    
    if answer == "List All Assigned Event":
        print("hal assigned event")
        # create_event() #hal. create event
    elif answer == "List All Event":
         listAllEvent()
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


 

