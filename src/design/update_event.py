from utils.helper import generateTitle, clear
from tabulate import tabulate
from src.service.event import Event

_eventService = Event()


def updateEvent():
    clear()
    generateTitle("Update Event", 14)

