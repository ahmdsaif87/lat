import random

angka_rahasia = random.randint(1,10)
percobaan = 1

while True:
    angka_tebakan = int(input('masukkan angka : '))
    if angka_tebakan == angka_rahasia :
        print('Benar')
        print('Selamat Tebakan and benar dalam percobaan ke = ', percobaan) 
        break
    elif angka_tebakan >= angka_rahasia :
        print('Terlalu Tinggi')
    elif angka_tebakan <= angka_rahasia :
        print('Terlalu Rendah')
    else :
        exit
    percobaan += 1