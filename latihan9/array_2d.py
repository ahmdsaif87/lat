import pandas as pd

data_penjualan = {
    'Senin' : [10,20,5],
    'Selasa' : [30,10,7],
    'Rabu' : [35,20,10],
    'Kamis' : [8,7,9],
    'Jumat' : [14,28,10],
    'Sabtu' : [10,20,5],
    'Minggu' : [5,7,8] 
}

df = pd.DataFrame(data_penjualan, index=['Es Teh', 'Gacoan', 'Hompimpa']).T

print('='*5,'Data penjualan Gacoan Tegal','='*5)
print(df)
print()

total_barang = df.sum(axis=0)

print('='*5,'Total penjualan tiap produk selama seminggu','='*5)
print(total_barang)
print()

total_penjualan_perhari = df.sum(axis=1)

print('='*5,'Total item yang terjual setiap harinya','='*5)
print(total_penjualan_perhari)
print()

penjualan_terbanyak = total_barang.idxmax()

print('='*5,'Item yang terjual terbanyak selama seminggu','='*5)
print(penjualan_terbanyak)
print()

hari_penjualan_terbanyak = total_penjualan_perhari.idxmax()

print('='*5,'Hari dengan penjualan terbanyak','='*5)
print(hari_penjualan_terbanyak)
print()