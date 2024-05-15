nama = str(input('Masukkan Nama : '))
umur = int(input('Masukkan Umur : '))
list_pekerjaan_ortu = ['Buruh', 'Serabutan']
pekerjaan_ortu = str(input('Pekerjaan Orang Tua : '))
gaji_ortu = int(input('Gaji Orang Tua : '))
ipk = float(input('Ipk : '))

if pekerjaan_ortu in list_pekerjaan_ortu and gaji_ortu <= 1000000 and ipk >= 2.7 and umur <= 25 :
    print('Memenuhi Syarat')
else :
    print('Tidak Memenuhi Syarat')
