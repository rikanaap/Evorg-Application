from utils.helper import generateTitle

def createRundown():
    generateTitle('Create rundown', 14)
    rundown_name = input("Rundown Name\t: ")
    description = input("Description\t: ")
    duration = input("Duration\t: ")
    index = input("Index Below\t: ")
    confirm = input("Confirm (yes/no)\t: ")

