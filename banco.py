class Conta:
    def __int__(self,titular, nConta, saldo):
        self.titular = titular
        self.nConta = nConta
        self.saldo = saldo

    def consultar(self):
        print(f'Titular: ',self.titular)
        print(f'Saldo: ',self.saldo)
        print("-" * 30)

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor


        else:
            print('Que dar uma esperto feioso !!! não pode não tem dindin')

    def transferir(self, valor, destino):
        self.saldo -= valor  #self.saldo = selt.saldo - valor
        destino.depositar(valor)




"""
conta1 = Conta("Juan", nConta:100,saldo:1000)
conta2 = Conta("Maricia, NConta:101, saldo:1000)
"""

conta1 = Conta()
conta1.titular = "eloiza"
conta1.nConta =201
conta1.saldo = 1000


conta2 = Conta()
conta2.titular ="Juan"
conta2.nConta =101
conta2.saldo =0


conta1.consultar()
conta1.transferir(1000,conta2)
conta1.consultar()


