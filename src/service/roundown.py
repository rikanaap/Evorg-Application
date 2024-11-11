from src.database.database import Database #Ini import, simpelnya ma ngambil dari file lain lah
class Roundown:
    def __init__(self):
        self.databaseModel = Database('roundown') #Ini initialize aja, kita kan pake roundown.json. Jadi ketik aja roundown
    def getAll(self):
        databaseData = self.databaseModel.getData() #Ambil data raw dari databaseModel
        databaseData = databaseData['datas'].values() #Ini ma gegara data list tu bentuknya object, gwa ganti ke array
        return databaseData