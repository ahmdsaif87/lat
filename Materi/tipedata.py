# Tipe data list
list_satu = ["Subandrio","Yanuar","Wildan","Fadil"]
list_dua = ["Pangkah","Slawi","Pakijangan","Batam Sari","Pangkah"]
list_tiga = ["Anthony","Onana","Mudryk"]

# Menambahkan data
list_satu.append("Bagas") # Menambahkan data pada akhir list
list_satu.insert(0,"Sigit") # Menambahkan data diantara list

# Menghapus data pada list
list_satu.remove("Yanuar") # Dengan memanggil datanya
del list_satu[3] # Dengan index

print(list_satu)

# Memanggil data
print(list_dua[0]) # dengan index
print(list_dua.index("Pakijangan")) # dengan data

# Menghitung
print(list_dua.count("Pangkah")) # Menghitung isi data
print(len(list_dua)) # Menghtung data dari sebuah list

# Mengurutkan data
list_tiga.sort() # Berdasarkan abjad a-z
list_tiga.reverse() # Berdasarkan abjad z-a
print(list_tiga)



# Tipe data dictionary
my_list = {'Nama':'Fermin Lopez','Umur':'99','Profesi':'Pesepakbola'}

print(my_list)


# Tipe data kombinasi
list_comb = [
    {'Nama':'Wildan','Asal':'Pakijangan'},
    {'Nama':'Abdel','Asal':'Pasar Pagi'},
    {'Nama':'Yanuar','Asal':'Kluwut'}
]

for i in list_comb:
    print('-',i['Nama'],i['Asal'])