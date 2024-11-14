import time
from utils.helper import generateTitle, clear
from src.service.user import User
from src.design.login import login

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
    enkripsi = userService.hashPassword(password)
    role = input("Pilih Role (spv/user)\t: ").lower()
    
    #validasi inputan role
    while role not in ["spv", "user"]:
        role = input("Role tidak valid. Masukkan 'spv' atau 'user'\t: ").lower()

    confirm = input("Apakah Anda yakin ingin mendaftar? (yes/no): ").lower()
    if confirm == "yes":
        data = {
            "username": username,
            "password": enkripsi,
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
