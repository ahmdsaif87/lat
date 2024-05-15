# Menghitung Gaji Karyawan 

nama = input('Masukkan Nama : ')
jam_kerja_sehari = int(input('Jam Kerja dalam sehari : '))
tarif_perjam = int(input('tarif perjam : '))
jam_kerja_perbulan = jam_kerja_sehari * 20

jumlah_gaji = jam_kerja_perbulan * tarif_perjam

print(f'Nama Karyawan : {nama}')
print(f'Gaji yang diterima : {jumlah_gaji:,}')