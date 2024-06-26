class Book:
    def __init__(self, judul, penulis, tahun_terbit):
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun_terbit = tahun_terbit
        
    def set_judul(self, judul):
        self.__judul = judul
        
    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_tahun_terbit(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit
    
    def informasi(self):
        return f'Judul Buku : {self.__judul}\nPenulis : {self.__penulis}\nTahun Terbit : {self.__tahun_terbit}'    
    
class Ebook(Book):
    def __init__(self, judul, penulis, tahun_terbit, ukuran_file):
        Book.__init__(self,judul, penulis, tahun_terbit)
        self.__ukuran_file = ukuran_file
    
    def set_ukuran(self, ukuran_file):
        self.__ukuran_file = ukuran_file
    
    def information(self):
        return f'{self.informasi()}\nUkuran File : {self.__ukuran_file}'