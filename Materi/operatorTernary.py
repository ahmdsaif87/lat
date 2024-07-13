# x = 10

# # CARA PERTAMA
# hasil = "Benar" if x > 5 else "salah"
# print(hasil)

# # CARA KEDUA
# if x > 5 :
#     print("Benar")
# else :
#     print("Kecil")
    
while True :
    tahun = int(input('Masukkan Tahun = '))
    print("Tahun kabisat") if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 4 == 0 else print('bukan kabisat')