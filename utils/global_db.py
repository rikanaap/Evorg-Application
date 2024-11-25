import json

class GlobalDatabase:
    def __init__(self):
        self.file_path = f"utils/global.json"
        self.DB_DATA = self.__getRawDataMain__()
        if not self.DB_DATA: raise ValueError("Failed to load database or model data.")
        self.DEFAULT_DATA = {
             "oneTimeLogin": False,
            "user_username": ""
        }

    def __getRawDataMain__(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        
    def __saveData__(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.DB_DATA, file, indent=4)
    def __updateData__(self):
        self.DB_DATA = self.__getRawDataMain__()
        
    def getData(self):
        self.__updateData__()
        return self.DB_DATA
    
    def checkIdentifier(self, identifier):
        self.__updateData__()
        return self.DB_DATA.get(identifier)
    
    def updateData(self, data):        
        self.DB_DATA = {**self.DB_DATA, **data }
        self.__saveData__()
        self.__updateData__()
        return self.DB_DATA
    
    def clearData(self): 
        self.DB_DATA = self.DEFAULT_DATA
        self.__saveData__()
        self.__updateData__()
        return True