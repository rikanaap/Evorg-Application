import datetime
from utils.helper import generateTitle

def register_participant():
    """Fungsi untuk registrasi peserta dengan username, password, dan role."""
    generateTitle("Registrasi Peserta", 14)

    username = input("Masukkan Username\t: ")
    password = input("Masukkan Password\t: ")

    role = input("Pilih Role (spv/user)\t: ").lower()
    while role not in ["spv", "user"]:
        role = input("Role tidak valid. Masukkan 'spv' atau 'user'\t: ").lower()

    confirm = input("Apakah Anda yakin ingin mendaftar? (yes/no): ").lower()
    
register_participant()
