namaKaryawan = input('Masukkan Nama : ')
Jabatan = input('Jabatan [Penyusun buku/Admin]: ').title()
kh = input('Harian [Y/T] ? ').upper()

if kh == "Y" :
    gb = 50000 if Jabatan == "Penyusun buku" else 100000 if Jabatan == "Admin" else 0
    kp = int(input('Berapa Hari Kerja : '))
    tg = gb * kp
elif kh == "T" :
    gb = 1500000 if Jabatan == "Penyusun buku" else 3000000 if Jabatan == "Admin" else 0
    tg = gb
else :
    print('Invalid')
    exit() 

tugas = "Merapihkan dan mengatur buku di Toko" if Jabatan == "Penyusun buku" else "Mengelola pesanan dan inventaris" if Jabatan == "Admin" else 0
pajak = 0.05 * tg
tp = tg - pajak

print('-' * 30) 
print(f'Nama : {namaKaryawan}')
print(f'Jabatan : {Jabatan}')
print(f'Tugasnya : {tugas}')
print(f'Pajak : {pajak:,}')
print(f'Total pendapatan : {tp:,}') 