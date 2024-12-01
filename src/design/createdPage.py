from utils.helper import clear, generateTitle
import inquirer
from src.design.table import tableCreatedEvent
from src.design.create_event import createEvent
from utils.local import getLocalUser

def display_event_list():
    from src.design.detail_event import detailEvent 
    from src.design.dashboard_spv import dashboard
    user = getLocalUser()
    createdEvent = user['createdEvent']
    
    clear()
    generateTitle("List All Created Event", 34)
    tableCreatedEvent(createdEvent)

    choices = ["Create Event"]
    if len(createdEvent) > 0: choices.append("Select Event")
    choices.append("Back")
    print()
    option =inquirer.list_input("Options", choices=choices)
    if option == "Create Event": return createEvent(display_event_list)
    elif option == "Select Event": 
        from src.design.select_event import selectEvent 
        selectEvent(lambda: detailEvent(display_event_list), user['assignedEvent'], createdEvent)
    elif option == "Back":
        return clear(), dashboard()
    else:
        print("Invalid choice. Please choose a valid option.")
        display_event_list()



