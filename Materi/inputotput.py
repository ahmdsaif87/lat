# INPUT

nama = float(input('Nama : '))
print(f"Nama : {nama} | Tipe data : {type(nama)}")

# OPERASI ARITMATIKA

a = int(input('Angka 1 : '))
b = int(input('Angka 2 : '))

print(f"Hasil Penjumalahn : {a+b}")
print(f"Hasil Pengurangan : {a-b}")
print(f"Hasil Perkalian : {a*b}")
print(f"Hasil Pembagian : {a/b}")
print(f"Hasil Pangkat : {a**b}")
print(f"Hasil Sisa Bagi (Modulus) : {a//b}")

# ARITMATIKA PENUGASAN

a = 5
a = 5
a += 5
a -= 5
a *= 5
a /= 5
a **= 5
print(a)

harga_barange = 15000
jumlah_barange = 10

total_harga = harga_barange * jumlah_barange
print(f'Harga Sebelum Diskon : {harga_barange}')
harga_barange -= 5000
print(f'Harga Sesudah Diskon : {harga_barange}')