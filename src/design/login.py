from utils.helper import generateTitle
import os, time
from src.service.user import User
from src.design.dashboard_user import dashboard
from src.design.dashboard_spv import dashboard as svp_dashboard

def login():
    userService = User()
    while True:
        generateTitle("LOGIN", 14)
        username = input("Masukan username\t: ")
        password = input("Masukan password\t: ")
        
        result = userService.validateUser(username, password)

        if result["success"]:
            user = result["user"]
            print(f"Selamat datang, {user['username']}!")
            print(f"Role Anda: {user['role']}")

            #cek role
            if user["role"].lower() == "spv":
                svp_dashboard()
            else:
                dashboard()
            break
            
        else:
            print("Login gagal:", result["message"])

        time.sleep(1)
        #refresh CLI jika akun salah
        if os.name == 'nt':  # Windows
            os.system("cls")
        else:
            os.system("clear")