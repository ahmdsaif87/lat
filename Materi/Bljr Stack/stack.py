# inisialisasi stack
data = []

# Menambahkan data pada stack
data.append("Wildan")
data.append("Yanuar")
data.append("Fadil")
data.append("Dede")


print(data)

data.pop() # mengambil/menghapus data yang diatas (pertama)
print(data)

print('Nilai peek/top = ', data[-1])

print('Ya' if data == 0 else 'Tidak')

print(len(data))