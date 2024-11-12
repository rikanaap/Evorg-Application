from utils.helper import generateTitle
import inquirer

def dashboard():
    print(generateTitle("Dashboard", 14))
    print("Welcome to the user's dashboard!!")

    answer = inquirer.list_input("Go to...", choices=["List All Assigned Event", "List All Event", "Logout"])
    
    if answer == "List All Assigned Event":
        print("hal assigned event")
        # create_event() #hal. create event
    elif answer == "List All Event":
        print("hal all event")
        # list_all_created_event() #hal list all created event
    elif answer == "Logout":
        print("logout")# logout()
    else:
        print("Invalid choice. Please choose a valid option.")
        dashboard()

