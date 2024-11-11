from src.service.roundown import Roundown
roundownService = Roundown()

def getAll():
    roundownData = roundownService.getAll()
    return print(roundownData['datas'].values())
