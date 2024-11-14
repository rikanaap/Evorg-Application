import hashlib
import time

# Pastikan untuk mengganti ini dengan implementasi yang sesuai jika Anda memiliki modul helper
def generateTitle(title, length):
    print(title.center(length, '='))

def clear():
    print("\n" * 100)  # Simulasi pembersihan layar

class User:
    def __init__(self):
        self.users = {}  # Menyimpan pengguna dalam dictionary

    def hash_password(self, password):
        # Menghitung hash SHA-256 dari password
        return hashlib.sha256(password.encode()).hexdigest()

    def registerUser (self, username, password, role):
        if username in self.users:
            return {"success": False, "message": "Username sudah terdaftar."}
        
        # Enkripsi password
        hashed_password = self.hash_password(password)
        self.users[username] = {"password": hashed_password, "role": role}
        return {"success": True, "message": "Registrasi berhasil."}

    def cekRegister(self, username):
        if username in self.users:
            return {"success": False, "message": "Username sudah terdaftar."}
        return {"success": True, "message": "Username tersedia."}

def register_participant():
    clear()
    userService = User()
    generateTitle("Registrasi Peserta", 30)

    username = input("Masukkan Username\t: ")

    # Cek apakah username sudah terdaftar
    check = userService.cekRegister(username)
    if not check["success"]:
        print(check["message"])
        time.sleep(1)
        return register_participant()

    password = input("Masukkan Password\t: ")
    role = input("Pilih Role (spv/user)\t: ").lower()
    
    # Validasi inputan role
    while role not in ["spv", "user"]:
        role = input("Role tidak valid. Masukkan 'spv' atau 'user'\t: ").lower()

    confirm = input("Apakah Anda yakin ingin mendaftar? (yes/no): ").lower()
    if confirm == "yes":
        result = userService.registerUser (username, password, role)
        if result["success"]:
            print("Registrasi berhasil.")
            time.sleep(1)
            # Panggil fungsi login di sini jika perlu
        else:
            print("Terjadi kesalahan saat menyimpan data:", result["message"])
    else:
        print("Registrasi dibatalkan.")
    time.sleep(1)

# Menjalankan fungsi registrasi peserta
register_participant()