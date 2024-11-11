from utils.helper import generateTitle
import os, time

while True:
    generateTitle("LOGIN", 14)

    username = input("Masukan username\t: ")
    password = input("Masukan password\t: ")

    if password != "xxx":
        print("Password salah, Coba lagi!")
        time.sleep(1)
        os.system("cls")
    else:
        break
