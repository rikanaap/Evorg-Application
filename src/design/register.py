import datetime
from utils.helper import generateTitle, clear

from utils.helper import generateTitle
import time

class User:
    def __init__(self):
        self.users = {}  

    def registerUser(self, username, password, role):
        if username in self.users:
            return {"success": False, "message": "Username sudah terdaftar."}
        
        self.users[username] = {"password": password, "role": role}
        return {"success": True, "message": "Registrasi berhasil."}

def register_participant():
    clear()
    userService = User()
    generateTitle("Registrasi Peserta", 14)

    username = input("Masukkan Username\t: ")

    # Cek apakah username sudah terdaftar di user.json
    check = userService.cekRegister(username)
    if not check["success"]:
        print(check["message"])
        time.sleep(1)
        return register_participant()

    password = input("Masukkan Password\t: ")
    role = input("Pilih Role (spv/user)\t: ").lower()
    
    #validasi inputan role
    while role not in ["spv", "user"]:
        role = input("Role tidak valid. Masukkan 'spv' atau 'user'\t: ").lower()

    confirm = input("Apakah Anda yakin ingin mendaftar? (yes/no): ").lower()
    if confirm == "yes":
        data = {
            "username": username,
            "password": password,
            "role": role,
        }
        result = userService.createOne(data)
        if result:
            print("Registrasi berhasil.")
            time.sleep(1)
            login()
        else:
            print("Terjadi kesalahan saat menyimpan data.")
    else:
        print("Registrasi dibatalkan.")
    time.sleep(1)
