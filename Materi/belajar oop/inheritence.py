class Manusia:  # Parent class
    def __init__(self, hidung, mata, rambut):
        self.hidung = hidung
        self.mata = mata
        self.rambut = rambut

class Pacar:
    def __init__(self, nama):
        self.nama = nama

class Yanuar(Manusia, Pacar):  # Child class
    def __init__(self, hidung, mata, rambut, kulit, nama):
        Manusia.__init__(self, hidung, mata, rambut)
        Pacar.__init__(self, nama)
        self.kulit = kulit

    def informasi(self):
        return f" Hidung : {self.hidung}, Mata : {self.mata}, Rambut : {self.rambut}, Kulit : {self.kulit}, Pacar : {self.nama}"

yanuar = Yanuar('Pesek', 'Sipit', 'Ikal', 'Sawo Matang', 'Seulgi')
print(yanuar.informasi())
