import modul as md

while True:
    print('Selamat datang di program Manajemen Stok Barang')
    print('Pilihan')
    print('1. Tambah data barang')
    print('2. Hapus data barang')
    print('3. Tampilkan data barang')
    print('4. Keluar')
    main = input('Masukkan pilihan: ')
    if main == '1':
        md.insert()
    elif main == '2':
        md.hapus_data()
    elif main == '3':
        md.tampilan_data()
    else:
        exit()