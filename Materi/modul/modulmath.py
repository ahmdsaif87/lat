import math

def penjumlahan(a,b):
    return a + b
def pengurangan(a,b):
    return a - b
def perkalian(a,b):
    return a * b
def pembagian(a,b):
    return a / b
def luaspersegi(a):
  return a * 4
def luaspersegipanjang(a,b):
  return a * b
def luaslingkaran(a): 
    return math.pi * a**2
def operasi ():
  while True:
    print("Pilih operasi matematika")
    print("1. Menghitung luas persegi")
    print("2. Menghitung luas persegi panjang")
    print("3. Menghitung luas lingkaran")
    pilihan = input("Masukkan pilhan anda: ")
    if pilihan == "1":
        a = int(input("Masukkan sisi: "))
        print(luaspersegi(a))
    elif pilihan == "2":
        a = int(input("Masukkan panjang: "))
        b = int(input("Masukkan lebar: "))
        print(luaspersegipanjang(a,b))
    elif pilihan == "3":
        a = int(input("Masukkan jari-jari: "))
        print(luaslingkaran(a))
    else:
        exit()