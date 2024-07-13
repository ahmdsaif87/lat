class Bank:
    def __init__(self, saldo):
        self.__saldo = saldo # enkapsulasi (mengunci dari dalam)
    
    def set_saldo(self, money):
        self.__saldo = money # kunci untuk membuka enkapsulasi
        
    def get_saldo(self):
        return self.__saldo
        
oren = Bank(1000)
oren.__saldo = 2000
print(f'Saldo Oren: {oren.__dict__}')

yanuar = Bank(1500)
yanuar.set_saldo(2000)
print(f'Saldo Yanuar: {yanuar.__dict__}')

fadil = Bank(1000)
fadil.set_saldo(2000)
print(fadil.get_saldo())