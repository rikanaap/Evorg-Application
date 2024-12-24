from utils.helper import generateTitle, clear, generateRoundown
from src.design.table import tableInputEvent, tableInputRundown
from utils.local import getLocalRundownId

def selectRundown(callback=None, rundownId=None, notes="Please select rundown"):
    clear()
    if not rundownId: rundownId = getLocalRundownId()
    selectedId = tableInputRundown(callback, rundownId, notes)  
    return selectedId