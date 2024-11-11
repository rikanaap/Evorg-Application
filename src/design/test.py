from src.service.roundown import Roundown
from tabulate import tabulate
import inquirer

roundownService = Roundown()

def getAll():
    roundownData = roundownService.getAll() #Ambil data dari service
    tableData = []
    for data in roundownData: #Loop data dari service
        for dataList in data['lists']:
            tableData.append([dataList['roundown_name'], dataList['duration'], dataList['description']]) #Masukin ke tableData (variable yang bakal dipake buat tabulate)
    print(tabulate(tableData))

def queryTest():
    print('Test query')
    inquirer.list_input("Pilih mas", choices=['Opsi 1', 'Opsi 2', 'Opsi 3'])

