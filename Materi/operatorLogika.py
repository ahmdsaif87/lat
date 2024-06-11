# OPERATOR LOGIKA
a = True
b = False

print("A And B : ", a and b) # LOGIKA AND
print("A And B : ", a or b) # LOGIKA OR
print("Not A : ", not a) # LOGIKA NOT
print("Not B : ", not b) # LOGIKA NOT

# Contoh
bayar_kuliah = bool(input("Wis Bayar Durung : "))
absensi = int(input("Absensimu Berapa : "))

if bayar_kuliah == True and absensi > 70 :
    print(10*'=', 'hasil', 10*'=')
    print("Masoook")
else :
    print("Balik Mana")
    
# OPERATOR IDENTITAS

# is = Mencetak True jika Objek dan Nilainya Sama
# is not = Mencetak True Jika Objek dan Nilainya Berbeda

a = 5 
b = 5
print(a is b)

tuple1 = (1,2,3,4)  # Tuple dinilai satu objek jika nilainya sama
tuple2 = (1,2,3,4)
print(tuple1 is tuple2)

list1 = [1,2,3,4] # walaupun nilainya sama List tetap dianggap beda objek
list2 = [1,2,3,4]
print(list1 is not list2)

# OPERATOR KEANGGOTAAN

pacar_putra = ['Fadil', 'Yanuar', 'Wildan', 'Dede']
print('Fadil' in pacar_putra)
print('fadil' in pacar_putra)
print('yanuar' not in pacar_putra)
