# menggunakan list
array_2d = [
    [1,2,3],
    [4,5,6]
]

print(array_2d[0][2])
print(array_2d[1][2])
print()

# menggunakan dictionary
data_kunjungan = {
    'Senin':[10,20,30],
    'Selasa':[40,50,60]
}

print(data_kunjungan['Senin'])
print(data_kunjungan['Senin'][0])

for hari,total in data_kunjungan.items():
    print(hari, total)
    print()
    
# menggunakan modul numpy
import numpy as np

array_numpy = np.array([
    [3,4,5],
    [6,7,8],
    [8,9,10]
])

print(array_numpy[2][1])
print(array_numpy[2,1])
print()

# menjumlahkan value
total_perbaris = np.sum(array_numpy, axis=0)
total_perkolom = np.sum(array_numpy, axis=1)

print(total_perbaris)
print(total_perkolom)
print()

# menampilkan nilai terbesar menggunakan index
terbesar_perbaris = np.argmax(array_numpy, axis=0)
terbesar_perkolom = np.argmax(array_numpy, axis=1)

print(terbesar_perbaris)
print(terbesar_perkolom)
print()

# menampilkan nilai terbesar menggunakan value
nilai_perbaris = np.max(array_numpy, axis=0)
nilai_perkolom = np.max(array_numpy, axis=1)

print(nilai_perbaris)
print(nilai_perkolom)
print()

# menggunakan modul pandas
import pandas as pd

# menggunakan list
array_pandas = pd.DataFrame([
    [5,6,7],
    [4,5,6],
    [7,8,9]
])
baris = ['Nasi Kuning', 'Ketoprak', 'Mawut']
kolom = ['Senin', 'Selasa', 'Rabu']

df = pd.DataFrame(array_pandas.values, index=baris, columns=kolom)

print(df) 
print()

# menggunakan dictionary
data = {
    'Senin' : [20,30,40],
    'Selasa' : [25,35,45]
}

df2 = pd.DataFrame(data, index=['Gacoan','Hompimpa','Es Teh'])
print(df2)
print()

total_nilai_tiap_baris = df2.sum(axis=0)
total_nilai_tiap_kolom = df2.sum(axis=1)

print(total_nilai_tiap_baris)
print(total_nilai_tiap_kolom)
print()

