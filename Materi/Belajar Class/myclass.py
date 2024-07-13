# class Motor:
#     def __init__(self, merek, model, warna, tahun) :
#         self.merek = merek
#         self.model = model
#         self.warna = warna
#         self.tahun = tahun
        
# motor1 = Motor('Honda', 'Supra Fit', 'Hitam', 2001)
# print(motor1.__dict__)

# motor2 = Motor('Yamaha', 'Mio Mirza', 'Merah', 2018)
# print(motor2.__dict__)


class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    def get_luas(self):
        return self.panjang * self.lebar
    
# hitung = PersegiPanjang(15, 10)
# print(hitung.get_luas())

# hitung2 = PersegiPanjang(20, 15)
# print(hitung2.get_luas())