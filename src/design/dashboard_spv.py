from utils.helper import generateTitle, clear
import inquirer
# from src.design.logout import logout

def dashboard():
    clear()
    print(generateTitle("Dashboard SPV", 14))
    print("Welcome to the SPV's dashboard!!")
    
    answer = inquirer.list_input("Go to...", choices=["Create New", "List All Created Event", "Logout"])
    
    if answer == "Create New":
        print("hal create event")
        # createEvent() #hal. create event
    elif answer == "List All Created Event":
        print("hal created")
        # list_all_created_event() #hal list all created event
    elif answer == "Logout":
        from src.design.first_page import first_page
<<<<<<< HEAD
        while True:
                confirm = input("Konfirmasi (yes/no): ").lower().strip()
                if confirm in ["yes", "y"]:
                    first_page()
                    break
                elif confirm in ["no", "n"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
     
=======
        yakin =  input("Yakin akan logout? (yes/no): ")
        if yakin == "yes":
          first_page()
        else:
          dashboard()
>>>>>>> 77a7769 (Ahmad | sinkron dara regis dengan .json dan login)
    else:
        print("Invalid choice. Please choose a valid option.")
        dashboard()



