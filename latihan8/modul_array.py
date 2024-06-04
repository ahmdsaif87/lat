import array as ar

nilai_siswa = []

def main():
    jumlah_siswa = int(input("Masukkan Jumlah siswa: "))
    total = 0
    for i in range (jumlah_siswa):
        nilai = int(input(f"Masukkan Nilai siswa ke- {i+1} "))
        nilai_siswa.append(nilai)
        
    print(f'Nilai rata-rata = {rata_rata()}')    
    print(f'Nilai tertinggi = {max()}')  
    print(f'Nilai terendah = {min()}')      
        
def rata_rata():
    rata = ar.sum(nilai_siswa)/len(nilai_siswa)
    return rata
    
def maksimal():
    maks = ar.max(nilai_siswa)
    return maks

def minimal():
    mini = ar.min(nilai_siswa)
    return mini 
    
main()












print('Dede Ganteng')
