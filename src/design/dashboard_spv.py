from utils.helper import generateTitle, clear
import inquirer

def dashboard():
    clear()
    print(generateTitle("Dashboard", 14))
    print("Welcome to the SPV's dashboard!!")
    
    answer = inquirer.list_input("Go to...", choices=["Create New", "List All Created Event", "Logout"])
    
    if answer == "Create New":
        print("hal create event")
        # create_event() #hal. create event
    elif answer == "List All Created Event":
        print("hal created")
        # list_all_created_event() #hal list all created event
    elif answer == "Logout":
        print("logout")# logout()
    else:
        print("Invalid choice. Please choose a valid option.")
        dashboard()



