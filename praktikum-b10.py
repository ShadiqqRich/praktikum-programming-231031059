import os
def judul():
    os.system("cls")
    print("Program Menghitung Volume dan Luas Permukaan".center(45))
    print("Bangun Ruang Balok".center(45))
    print()

def inputan():
    p = float(input("Masukkan Panjang: "))
    l = float(input("Masukkan Lebar: "))
    t = float(input("Masukkan Tinggi: "))
    return p,l,t

def hitung(p,l,t):
    vol = p*l*t
    luas_surf = 2*(p*l + p*t + l*t)
    luas_non_tutup = luas_surf - p*l
    return vol,luas_surf,luas_non_tutup

def tampilan(pesan,nilai):
    print(f"Hasil {pesan} : {nilai}")
    
def pilihan():
        pilih = input("Apakah lanjutkan [y/n]")
        if pilih == "y":
            a = True
        else:
            a = False
            print("Terima kasih!")
        return a

def main():
    judul()                                      # Judul
    p,l,t = inputan()                            # Inputan
    vol,luas_surf,luas_non_tutup = hitung(p,l,t) # Hitung
    tampilan("Volume",vol)                       # Tampilan
    tampilan("Luas Permukaan",luas_surf)
    tampilan("Luas permukaan tanpa tutup",luas_non_tutup)
    a = pilihan()                                # Pilihan
    return a
    
a = True
while a:
     a = main()