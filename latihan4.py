namaKaryawan = input('Masukkan namamu : ')
jabatanMu = input('Apa Jabatanmu [Design/Programmer/Resource]:').lower()
status = input('Apakah sudah menikah [Y/T] : ').title()

gp = 5000000 if jabatanMu == "design" or jabatanMu == "resource" else 10000000 if jabatanMu == "programmer" else 0

if gp == 0:
    print("invalid")
    exit()
    
if status == 'Y' :
    tunjangan = 0.2 * gp   
elif status == "N":
    tunjangan = 0
else :
    print('tidak')
    exit()
    
gajiKotor = gp + tunjangan
pajak = 0.1 * gajiKotor
totalPendapatan = gp - pajak
    
print(f'{namaKaryawan}')
print(f'{jabatanMu}')
print(f'Gaji pokok : {gp}')
print(f'Tunjangan : {tunjangan}')
print(f'Gaji kotor : {gajiKotor}')
print(f'Pajak : {pajak}')
print(f'Total pendapatan = {totalPendapatan}')