from utils.helper import generateTitle, clear
import inquirer
# from src.design.login import login
# from src.design.register import register_participant
# import inquirer

def first_page():
    generateTitle("Authentikasi", 7)
    answer = inquirer.list_input("Go to...", choices=["Login", "Register"])
  
    # if answer == "Login":
    #     login()
    # elif answer == "Register":
    #     register_participant()
    # else:
    #     print("Invalid choice. Please choose a valid option.")
    #     first_page()