from utils.helper import generateTitle, clear
import time
import inquirer
from src.service.user import User
from utils.global_db import GlobalDatabase
from src.design.dashboard_user import dashboard
from src.design.dashboard_spv import dashboard as spv_dashboard

def login():
    clear()
    userService = User()
    globalDb = GlobalDatabase()
    while True:
        generateTitle("LOGIN", 14)
        username = input("Masukan username\t: ")
        password = input("Masukan password\t: ")
        
        enkripsi = userService.hashPassword(password)
        
        result = userService.validateUser(username, enkripsi)

        if result["success"]:
            clear()
            user = result["user"]
            print(f"Selamat datang, {user['username']}!")
            print(f"Role Anda: {user['role']}")

            confirmRemember = inquirer.confirm(f"Remember me as {user['username']}?", default=True)
            print(confirmRemember)
            if confirmRemember: globalDb.updateData({ "oneTimeLogin": True, "user_username": user['username']})
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