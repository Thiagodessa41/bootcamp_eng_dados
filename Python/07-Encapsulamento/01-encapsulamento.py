# encapsulamesnto conceito de algo publico e privado de um codigo, proteger dados
# por convenção o (_) indentifica algo privado em python
# exemplo saldo da conta bancária dado privado

class Conta:
    def __init__(self,nro_agencia, saldo=0):
        self._saldo = saldo # (_saldo) variável dado privado
        self.nro_agencia = nro_agencia


    def depositar(self, valor):
        #...verificações necessárias
        self._saldo += valor


    def sacar(self, valor):
        #...verificações necessárias
        self._saldo -= valor

    def mostrar_saldo(self):
        #...verificações necessárias
        return self._saldo    


conta  = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())