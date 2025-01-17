import json
class Database:
    def __init__(self, file_name, options={}):
        self.file_path = f"src/database/json/{file_name}.json"
        self.file_model_path = f"src/database/json/models/{file_name}.json"

        self.DB_DATA = self.__getRawDataMain__()
        self.DB_MODEL_DATA = self.__getRawDataModel__()
        if not self.DB_DATA or not self.DB_MODEL_DATA: raise ValueError("Failed to load database or model data.")

        self.model_idented = options.get('model_idented', False)
        self.identifier_unique = options.get('identifier_unique', True)

    def __getRawDataMain__(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return False
    
    def __getRawDataModel__(self):
        try:
            with open(self.file_model_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        
    def __saveData__(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.DB_DATA, file, indent=4)

    def __updateData__(self):
        self.DB_DATA = self.__getRawDataMain__()
        self.DB_MODEL_DATA = self.__getRawDataModel__()

    def getModel(self):
        self.__updateData__()
        return self.DB_MODEL_DATA
    def getData(self, assigned=None, created=None):
        self.__updateData__()
        dataFilter = self.DB_DATA
        if assigned is not None or created is not None:
            dataFilter['datas'] = {}
            if assigned is not None: 
                for identifier in assigned: dataFilter['datas'][identifier] = self.checkIdentifier(identifier)
            if created is not None: 
                for identifier in created: dataFilter['datas'][identifier] = self.checkIdentifier(identifier)
        return self.DB_DATA if len(dataFilter) < 1 else dataFilter
    
    def getCurrentId(self):
        self.__updateData__()
        return self.DB_DATA['current_id']
    
    def checkIdentifier(self, identifier):
        self.__updateData__()
        return self.DB_DATA['datas'].get(identifier)
    
    def addData(self, data, identifier=None):
        self.DB_DATA['current_id'] += 1
        identifier = identifier if identifier is not None else self.DB_DATA['current_id']
        
        identiferExist = self.checkIdentifier(str(identifier))
        if self.identifier_unique and identiferExist: return False
        if data:
            if self.model_idented: 
                if not identiferExist: self.DB_DATA['datas'][identifier] = []
                self.DB_DATA['datas'][identifier].append({**self.DB_MODEL_DATA, **data})
            else: self.DB_DATA['datas'][identifier] = {**self.DB_MODEL_DATA, **data }

        self.DB_DATA['current_id'] += 1
        self.__saveData__()
        self.__updateData__()
        return self.checkIdentifier(identifier)
    
    def updateData(self, identifier, data, index=None):
        identifierData = self.checkIdentifier(identifier)
        if not identifierData: return False
        
        if self.model_idented: 
            if index is None or not (0 <= index < len(identifierData)): return False
            self.DB_DATA['datas'][identifier][index] = data
        else: self.DB_DATA['datas'][identifier] = {**identifierData, **data }

        self.__saveData__()
        self.__updateData__()
        return self.checkIdentifier(identifier)
    
    def deleteData(self, identifier, options={}):
        hardDelete = options.get('hard', False)
        indexDelete = options.get('index', None)

        identifierData = self.checkIdentifier(identifier)
        if not identifierData: return False
        
        if hardDelete: del self.DB_DATA['datas'][identifier]
        if indexDelete is not None: 
            if 0 <= indexDelete < len(identifierData): self.DB_DATA['datas'][identifier].pop(indexDelete)
            else: return False
        
        self.__saveData__()
        self.__updateData__()
        return self