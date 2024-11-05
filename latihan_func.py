"""
Nama: Ahmad Zaelani
NIM: 2410023
Kelas: 1A
"""

def volume_tabung(r,t):
    vol = 22/7 * r * r * t
    return vol

jari = int(input("Masukan jari-jari tabung: "))
tinggi = int(input("Masukan tinggi tabung: "))

print(volume_tabung(jari, tinggi))
    
