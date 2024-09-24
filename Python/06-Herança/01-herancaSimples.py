# classe veiculo
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        #caracteristicas
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # comportamentos metodos
    def ligar_motor(self):
        print("Ligando motor!")   

    def __str__(self):
        return f"{self.__class__.__name__}: {' , '.join([f'{chave}={valor}' for chave, valor in self. __dict__.items()])}"    


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__( cor, placa, numero_rodas) #super() invoca um método da classe pai
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!")


moto = Motocicleta (" Preta ", "ABC-1234 ", 2)
moto.ligar_motor()

carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "edf-7756", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
print(carro)
print(moto)