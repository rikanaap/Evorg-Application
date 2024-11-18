import json
class Database:
    def __init__(self, file_name, options={}):
        self.file_path = f"src/database/json/{file_name}.json"
        self.file_model_path = f"src/database/json/models/{file_name}.json"

        self.DB_DATA = self.__getRawDataMain__()
        self.DB_MODEL_DATA = self.__getRawDataModel__()
        if not self.DB_DATA or not self.DB_MODEL_DATA: raise ValueError("Failed to load database or model data.")

        self.model_idented = options.get('indent_model', False)
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

    def getModel(self):
        return self.DB_MODEL_DATA
    
    def getData(self, id=None):
        if id:
            return self.DB_DATA['datas'].get(id, None)
        return self.DB_DATA['datas']
    
    def getCurrentId(self):
        return self.DB_DATA['current_id']
    
    def checkIdentifier(self, identifier):
        return self.DB_DATA['datas'].get(identifier)
    
    def addData(self, data, identifier=None):
        self.DB_DATA['current_id'] += 1
        identifier = identifier if identifier is not None else self.DB_DATA['current_id']
        
        identiferExist = self.checkIdentifier(identifier)
        if self.identifier_unique and identiferExist: return False
        
        if self.model_idented: 
            if identiferExist: self.DB_DATA['datas'][identifier] = []
            self.DB_DATA['datas'][identifier].append({**self.DB_MODEL_DATA, **data})
        else: self.DB_DATA['datas'][identifier] = {**self.DB_MODEL_DATA, **data }

        self.__saveData__()
        return self.checkIdentifier(identifier)
    
    def updateData(self, identifier, data, index=None):
        identifierData = self.checkIdentifier(identifier)
        if not identifierData: return False
        
        if self.model_idented: 
            if index is None or not (0 <= index < len(identifierData)): return False
            self.DB_DATA['datas'][identifier].insert(index, { **identifierData, **data })
        else: self.DB_DATA['datas'][identifier] = {**identifierData, **data }
        self.__saveData__()
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
        return self
        
    def addUser(self, data, identifier=None):
        identifier = data.get("username")
        
        identiferExist = self.checkIdentifier(identifier)
        if self.identifier_unique and identiferExist: return False
        
        if self.model_idented: 
            if identiferExist: self.DB_DATA['datas'][identifier] = []
            self.DB_DATA['datas'][identifier].append({**self.DB_MODEL_DATA, **data})
        else: self.DB_DATA['datas'][identifier] = {**self.DB_MODEL_DATA, **data }

        self.__saveData__()
        return self.checkIdentifier(identifier)
