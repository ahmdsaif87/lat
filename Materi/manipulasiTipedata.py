# Memanipulasi String
contoh1 = "Waroeng"
contoh2 = "Steak"
int1 = 15

print(contoh1 + " " + contoh2)
print((contoh1 + " ") * 20) 
print(contoh2 + " ")
print(contoh2 + " " + str(int1))

# Menggabungkan beberapa data
list1 = ['aku','seorang','gosling']
kalimat = " ".join(list1)
print(kalimat)

# Memisahkan sebuah String menjadi data List
list2 = "aku Ryan Gosling"
kalimat2 = list2.split()
print(kalimat2)

# Merubah isi data
kalimat3 = list2.replace("Gosling", "Kurnia")
print(kalimat3)

# Mengubah penulisan data
print(list2.upper())
print(list2.lower())
print(list2.capitalize())
print(list2[0:11])
print(list2.title())

# Mengubah peruangan
duit = 100000000
print('{:,}'.format(duit))
print('{:.2f}'.format(duit))
print('{:,.2f}'.format(duit))

print(f'Rp.{duit:,}')

#
okok = input("Kamu suka bara bere nggak ? [Suka/Tidak] : ").upper()
print(okok)