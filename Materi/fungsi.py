def luaspersegi(a):
  return a * 4
def luaspersegipanjang(a,b):
  return a * b
def luaslingkaran(a,b):
  return a * b 
  
def operasi ():
  while True:
    print("Pilih operasi matematika")
    print("1. Menghitung luas persegi")
    print("2. Menghitung luas persegi panjang")
    print("3. Menghitung luas lingkaran")
    pilihan = input("Masukkan pilhan anda: ")
    if pilihan == "1":
      print("Masukkan Sisi: ")
      print(luaspersegi(a))
    elif pilihan == "2":
      print("Masukkan panjang: ")
      print("Masukkan lebar: ")
      print(luaspersegipanjang(a,b))
    else:
      exit()