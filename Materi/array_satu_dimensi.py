nilai_siswa = [90,80,70,65]

print(nilai_siswa[1])

nilai_siswa.append(85)

nilai_siswa[0] = 95

rata_rata = sum(nilai_siswa)/len(nilai_siswa)

print(nilai_siswa)
print(len(nilai_siswa))
print(sum(nilai_siswa))
print(max(nilai_siswa))
print(min(nilai_siswa))
print(rata_rata)

nilai_diatas_rata_rata = sum(True for i in nilai_siswa if i > rata_rata)
print(nilai_diatas_rata_rata)