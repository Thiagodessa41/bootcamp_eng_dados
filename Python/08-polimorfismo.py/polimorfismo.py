"""polimorfismo 
significa ter muitas formas, na programação, polimorfismo significa o mesmo nome de função,
mas assinaturas diferentes sendo usado para tipos diferentes
"""


"""
    na herança a classe fiha herda métodos da (classe pai passaro)
    é possivel modificar um método em uma (classe filha avestruz) herdada da classe pai
    os métodos herdados da classe pai não encaixa perfeitamente na classe filha
"""
class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj): #polimorfismo está aqui
    obj.voar()          #voar se comporta diferente de acordo com passaro


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
