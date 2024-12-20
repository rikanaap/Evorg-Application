from src.database.database import Database #Ini import, simpelnya ma ngambil dari file lain lah
class Roundown:
    def __init__(self):
        self.databaseModel = Database('roundown', { 'model_idented': True , 'identifier_unique': False}) #Ini initialize aja, kita kan pake roundown.json. Jadi ketik aja roundown
        
    def getAll(self):
        databaseData = self.databaseModel.getData() #Ambil data raw dari databaseModel
        databaseData = databaseData['datas'].values() #Ini ma gegara data list tu bentuknya object, gwa ganti ke array
        return databaseData
    
    def getOne(self, id):
        return self.databaseModel.checkIdentifier(id)
    
    def updateData(self, id, data):
         indexData = data['index_below']
         del data['index_below']
         return self.databaseModel.updateData(id, data, indexData)

    def getRawAll(self):
        return self.databaseModel.getData()
    def createOne(self, id, data):
        return self.databaseModel.addData(data, id)
    
    