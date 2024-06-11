# Perulangan for

data = ['Putra','Yanuar','Fadil','Wildan','Dede']
datanos = [1,2,3,4]
me = 'Aku seorang kapiten'

for datas in data :
    print(datas)
print('\n')

for aku in me :
    print(aku)
print('\n')

for i in range(2,5) :
    print(i)
print('\n')

for index, datas in  enumerate(data) :
    print(index, datas)
print('\n')

for datan, datas in zip(datanos, data) :
    print(datan, datas)
print('\n')

dict = {'Nama':'Ahmad Saifi Khayatu Ulumuddin','NIM':23090112}

for label, values in dict.items() :
    print(label, ':', values) # Ngeprint Label dan Value
print('\n')

for value in dict.values() :
    print(value) # Ngeprint Value doang
print('\n')

for dicti in dict :
    print(dicti)
print('\n')

for i in range(10) :
    if i % 2 == 0 :
        print(i,'Bilangan Genap')
    else :
        print(i,'Bilangan Ganjil')
print('\n')



# Perulangan while

i = 1
while i <=10 :
    print(i)
    i += 1
print('\n')

totalPerulangan = 0
while True :
    main = input('Pernah nggak ready ? ').lower()
    if main == 'ready' :
        break
    totalPerulangan += 1
print('Total perulangan : ', totalPerulangan)
print('\n')

i = 1
while i <= 10 :
    if i == 4 :
       i += 1
       continue
    print(i)
    i += 1
