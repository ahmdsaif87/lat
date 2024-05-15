data = []

def insert():
    print('=' * 20)
    nama_barang = input("Nama barang: ")
    stok_barang = int(input("Stok barang: "))
    dict_barang = {'Nama barang': nama_barang,'Stok barang': stok_barang}
    data.append(dict_barang)
    print('=' * 20)

def tampilan_data():
    for i in data:
        print('=' * 20)
        print('-','Nama barang: ',i['Nama barang'],',','Stok barang: ',i['Stok barang'])
        print('=' * 20)
        
def hapus_data():
    print('=' * 20)
    ok = int(input('Index ke: '))
    del data[ok]
    print(f'Barang {ok} telah dihapus')
    print('=' * 20)