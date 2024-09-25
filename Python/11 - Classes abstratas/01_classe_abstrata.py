"""Interfaces elas definem oque uma classe deve fazer e não como,
o conceito de interface é definir um contrato, onde são declarados os métodos (o deve ser feito)
e suas respectivas assinaturas, em python utilizamos classes abstratas para criar contratos, classes
abstratas não podem ser instanciadas
"""

# módulo ABC

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self): #MÉTODO ABSTRATO
        pass

    @abstractmethod
    def desligar(self): #MÉTODO ABSTRATO
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
