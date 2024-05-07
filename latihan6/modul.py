def penjumlahan(a,b):
    return a + b
def pengurangan(a,b):
    return a - b
def perkalian(a,b):
    return a * b
def pembagian(a,b):
    return a / b   
def operasi(): 
    while True:
        print('Pilih operasi matematika:')
        print('1. Penjumlahan')
        print('2. Pengurangan')
        print('3. Perkalian')
        main = input('Masukkan pilihan Anda : ')
        if main == '1':
            a = int(input('Masukkan bilangan pertama : '))
            b = int(input('Masukkan bilangan kedua : '))
            print(penjumlahan(a,b))
        elif main == '2':
            a = int(input('Masukkan bilangan pertama : '))
            b = int(input('Masukkan bilangan kedua : '))
            print(pengurangan(a,b))
        elif main == '3':
            a = int(input('Masukkan bilangan pertama : '))
            b = int(input('Masukkan bilangan kedua : '))
            print(perkalian(a,b))
        else:
            exit()