from utils.helper import clear, generateTitle
import inquirer
from src.design.table import tableCreatedEvent
from src.design.create_event import createEvent
from src.design.select_event import selectEvent 
 
def display_event_list():
    
    
    clear()

    generateTitle("List All Created Event", 34)

    tableCreatedEvent()
        
    option =inquirer.list_input("Options", choices=["Create Event", "Select Event"])
    if option == "Create Event":return createEvent()
    elif option == "Select Event": return selectEvent()

    else:
        print("Invalid choice. Please choose a valid option.")
        display_event_list()





