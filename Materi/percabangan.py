nilai = int(input('Masukkan angka dengan range dari 0-999 : '))

if nilai < 0 or nilai > 999 :
    print('Anda Salah')
    exit()
    
print('Fadil')

# penggunaan elif
nilai = int(input('Masukkan nilai anda : '))

if nilai >= 85 :
    print('A')
elif nilai < 85 :
    print('B')
elif nilai <= 75 :
    print('C')
    
# penggunaan else
bukber = bool(input('Apakah 30k Worth it ? : '))

if bukber == True :
    print('Bolehhhh')
else :
    print('larangggg')
    
# percabangan bersarang
umur = int(input('Masukkan umurumu : '))

if umur >= 17 :
    undangan = input('Apakah anda membawa undangan pencoblosan [Y/T] ? ').upper()
    if 'Y' :
        print('anda boleh masuk')
    else :
        print('anda pulang dan bawa undangannya')
else :
    print('Anda tidak boleh coblos')