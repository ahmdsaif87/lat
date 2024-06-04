data = []
undo = []

while True:
    print()
    print(f"Riwayat pencarian saat ini : {data}")
    print("Pilihan:")
    print("1. Tambah Pencarian")
    print("2. Hapus pencarian Terakhir")
    print("3. Undo")
    print("4. Keluar")
    
    pilihan = input("PIlih Operasi [1/2/3/4] = ")
    if pilihan == "1":
        penambah = input("Masukkan Kata Kunci Pencarian = ")
        data.append(penambah)
        print(f"'{penambah}' ditambahkan keriwayat pencarian")
    elif pilihan == "2":
        data_undo = data.pop()
        undo.append(data_undo)
        print(f"'{data_undo}' telah dihapus dari riwayat pencarian")
    elif pilihan == "3":
        undoo = undo.pop()
        data.append(undoo)
        print(f"'{undoo}' telah dikembalikan keriwayat pencarian")
    else:
        break