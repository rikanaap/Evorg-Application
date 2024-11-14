from utils.helper import generateTitle, clear
import inquirer


def dashboard():
    clear()
    print(generateTitle("Dashboard User", 14))
    print("Welcome to the user's dashboard!!")

    answer = inquirer.list_input("Go to...", choices=["List All Assigned Event", "List All Event", "Logout"])
    
    if answer == "List All Assigned Event":
        print("hal assigned event")
        # create_event() #hal. create event
    elif answer == "List All Event":
        print("hal all event")
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

