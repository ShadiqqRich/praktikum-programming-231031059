import os
os.system("cls")

a = True

while a:
    jawab = input("Apakah ingin melanjutkan? (y/n)")
    if jawab == "y":

        os.system("cls")
        print("Selamat Datang lagi!")
        a = True

    elif jawab == "n":

        print("Sampai ketemu lagi :D")
        a = False

    else:

        print("Jangan aneh-aneh deh :,)")  
        a = True  

