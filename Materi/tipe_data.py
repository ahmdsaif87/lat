# # TIPE DATA STRING
# kocak = "gay"
# kocakk = "support LGBT"
# print("Fadil adalah ", kocak , "dan ", kocakk)
# print(f"Fadil {kocak}")

# # TIPE DATA FLOAT
# uang_saku_fadil = 25.000
# uang_saku_putra = 25.000
# print(uang_saku_fadil + uang_saku_putra)

# # TIPE DATA BOOLEAN


# # TIPE DATA LIST 
# cowoPutra = ['Fadil', 'Wildan', 'Yanuar', 'Dede', 'Yusuf']
# cowoPutra[3]= 'Ikhsan'
# print(cowoPutra[0])

# # TIPE DATA TUPLE


# # TIPE DATA DICTIONARY
# Biodata = {'Nama':'Wahyu Fadil','Kesukaan':'Putra'}
# Biodata['Kesukaan']
# print(['Kesukaan'])

# Meminta pengguna untuk memasukkan nilai boolean (True/False) apakah kartu keluarga harus ada
kartu_keluarga_ada = input("Apakah kartu keluarga harus ada? (True/False): ").lower() == 'true'

# Memeriksa apakah kartu keluarga ada
if kartu_keluarga_ada:
    print("Kartu keluarga sudah ada.")
else:
    print("Kartu keluarga belum ada.")
