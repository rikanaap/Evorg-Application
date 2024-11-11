import json
class Database:
    def __init__(self, file_name):
        self.file_path = f"src/database/json/{file_name}.json"
        self.file_model_path = f"src/database/json/models/{file_name}.json"
        self.DB_DATA = self.__getRawData__(self.file_path)
        self.DB_MODEL_DATA = self.__getRawData__(self.file_model_path)
        if(not self.DB_DATA): return False
        if(not self.DB_MODEL_DATA): return False

    def __getRawData__(self, path):
        with open(self.file_path, 'r') as file:
            return json.load(file)
        return False

    def getModel(self):
        return self.DB_MODEL_DATA
    def getData(self):
        return self.DB_DATA
