import shutil

def tittle(nama):
    # Mendapatkan lebar terminal saat ini
    lebar_terminal = shutil.get_terminal_size().columns
    
    # Menghitung panjang nama dengan tanda "=" di kedua sisi
    panjang_nama = len(nama) + 2  # Ditambah 2 untuk spasi di kedua sisi nama
    
    # Menghitung jumlah tanda "=" di kiri dan kanan
    sisa = lebar_terminal - panjang_nama
    kiri = sisa // 2
    kanan = sisa - kiri
    
    # Membuat garis
    garis = "=" * kiri + f" {nama} " + "=" * kanan
    print(garis)