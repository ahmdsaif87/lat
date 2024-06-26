antrian = []

def antrian_pertama():
    if len(antrian) < 1:
        return 'Kosong'
    else:
        return antrian[0]

def tambah_antrian(item):
    antrian.append(item)
    
def antrian_selanjutnya():
    if len(antrian) < 2:
        return 'Kosong'
    else:
        return antrian[1]

def lihat_antrian():
    if len(antrian) == 0:
        print('Antrian Kosong')
    else:
        for index,value in enumerate(antrian):
            print(f'{index}: {value}')

def tampilan():
    while True:
        print('Antrian Sekarang: ', antrian_pertama())
        print('Antrian selanjutnya: ', antrian_selanjutnya())
        print('Pilihan')
        print('1. Tambah Antrian')
        print('2. Antrian Selanjutnya')
        print('3. Lihat Antrian')
        print('4. Keluar')
        main = input('Masukkan Pilihan:')
        if main == '1':
            item = input('Masukkan nama pelanggan: ')
            tambah_antrian(item)
            print('=' * 20)
        elif main == '2':
            print(f'Antrian selanjutnya adalah {antrian_selanjutnya()}')
            print('=' * 20)
        elif main == '3':
            print('List Antrian:')
            lihat_antrian()
            print('=' * 20)
        elif main == '4':
            break
        else:
            print('Inputan salah')
            print('=' * 20)
            
tampilan()