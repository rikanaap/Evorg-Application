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
    """Fungsi untuk registrasi peserta dengan username, password, dan role."""
    clear()
    userService = User()
    generateTitle("Registrasi Peserta", 14)

    username = input("Masukkan Username\t: ")
    password = input("Masukkan Password\t: ")

    role = input("Pilih Role (spv/user)\t: ").lower()
    while role not in ["spv", "user"]:
        role = input("Role tidak valid. Masukkan 'spv' atau 'user'\t: ").lower()

    confirm = input("Apakah Anda yakin ingin mendaftar? (yes/no): ").lower()
    if confirm == "yes":
        result = userService.registerUser(username, password, role)
        
        if result["success"]:
            print("Registrasi berhasil!")
        else:
            print("Registrasi gagal:", result["message"])

        time.sleep(1)
    else:
        print("Registrasi dibatalkan.")
        time.sleep(1)

#register_participant()
