print(f'Tugas 2 : Buat Program')
print()

print(f'2. Program Selisih Waktu')

jm1 = int(input("Masukkan jam pertama: "))
mnt1 = int(input("Masukkan menit pertama: "))


jm2 = int(input("Masukkan jam kedua: "))
mnt2 = int(input("Masukkan menit kedua: "))

total_jam = (jm1 - jm2)
total_menit = (mnt1 - mnt2)

if total_menit <= 0:
    total_menit = total_menit % 60
    total_jam = total_jam -1
    
    
print("Jumlah selisih waktu: 0{}:{}".format(total_jam,total_menit))