print("praktikum-b4")

print()
nama    = "MUHAMMAD SHADIQ DZAKWAN SYADDAD"
nim     = "231031059"
meet    = "praktikum 4"
prodi   = "Sistem informasi B"
email   = "cupenepen46@gmail.com"
tgl     = "11 oktober 2023"
sp = 40
print(nama,"panjangnya adalah:",len(nama))

# print(len(nama))
print("-"*sp)
print(nama.center(sp))
print(nim.center(sp))
print("\n"*2)

print(prodi.rjust(sp)+ f"\r{meet}")
print(email.rjust(sp)+ f"\r{tgl}")
print("-"*sp)

paragraf = """Halo, selamat datang perkenalkan nama
saya {} dengan NIM{} dari prodi {},
Ini adalah file {},"""

p = paragraf.format(nama,nim,prodi,meet)
print(p)

print("--------8++++++++")
x = 9 #input
hasil = x>8
print(x,"hasilnya adalah",hasil)

print("--------8++++++++")
x = 9 #input
hasil = x<8
print(x,"hasilnya adalah",hasil)

print("--------4++++++++8--------")
x = 5 #input
#cek1 = x>4
cek1 = x>4
# cek2 = x<8
cek2 = x<8
# hasil = cek1 and cek2 -->true
hasil = cek1 and cek2
# cetak hasil
print(x,"hasilnya adalah",hasil)

print("++++++++4--------8++++++++")
x = 2 #input
# cek1 = x>4
cek1 = x>4
# cek2 = x>8
cek2 = x<8
# hasil = cek1 or cek2 --> true
hasil = cek1 or cek2
# cetak hasil
print(x,"hasilnya adalah",hasil)



