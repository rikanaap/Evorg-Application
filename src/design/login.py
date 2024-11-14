from utils.helper import generateTitle, clear
import time
from src.service.user import User
from src.design.dashboard_user import dashboard
from src.design.dashboard_spv import dashboard as spv_dashboard

def login():
    clear()
    userService = User()
    while True:
        generateTitle("LOGIN", 14)
        username = input("Masukan username\t: ")
        password = input("Masukan password\t: ")
        
        enkripsi = userService.hashPassword(password)
        
        result = userService.validateUser(username, enkripsi)

        if result["success"]:
            user = result["user"]
            print(f"Selamat datang, {user['username']}!")
            print(f"Role Anda: {user['role']}")

            #cek role
            if user["role"].lower() == "spv":
                spv_dashboard()
            else:
                dashboard()
            break
            
        else:
            print("Login gagal:", result["message"])

        time.sleep(1)
        #refresh CLI jika akun salah
        clear()