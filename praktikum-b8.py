import os
os.system("cls")

pwd_benar = "si23b"
a = True
i = 0
limit = 3

while a:
    i += 1
    pwd = input("Masukkan Password: ")
    if pwd == pwd_benar:
        print("Selamat anda Login!")
        a = False
    else:
        if i == limit:
            a = False
            print("Anda kehabisan kesempatan")
        else:
            print("Password Salah")
            print(f"Kesempatan anda tersisa {limit-i} kali")      

