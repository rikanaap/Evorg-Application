import datetime

def register_participant():
    """Fungsi untuk registrasi peserta dengan username, password, dan role."""
    print("=== Registrasi Peserta ===")
    
    username = input("Masukkan Username\t: ")
    password = input("Masukkan Password\t: ")

    role = input("Pilih Role (spv/user)\t: ").lower()
    while role not in ["spv", "user"]:
        role = input("Role tidak valid. Masukkan 'spv' atau 'user'\t: ").lower()

    confirm = input("Apakah Anda yakin ingin mendaftar? (yes/no): ").lower()
    if confirm == "yes":
       
        participant = {
            "username": username,
            "password": password,
            "role": role,
            "registration_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"Registrasi berhasil! Data peserta:")
        print(f"Username: {participant['username']}")
        print(f"Role: {participant['role']}")
        print(f"Waktu Registrasi: {participant['registration_time']}")
    else:
        print("Registrasi dibatalkan.")

register_participant()
