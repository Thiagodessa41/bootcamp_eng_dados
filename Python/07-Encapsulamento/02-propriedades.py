#Property ()   cria atributos gerenciados em suas classes, pode usar atributos gerenciados, 
# também conhecidos como propriedades, quando precisar modificar sua implementação interna 
# sem alterar a API pública da classe
# exemplo vc tem uma (var = nome) agora vc quer que venha com sobrenome, e vc cria uma propriedade python
# automaticamente ele junta 1° nome sobrenome
# sintaxe depurador @property  @setter   @delete
# depurador uma função que executa antes da sua função

class Foo:
    def __init__(self, x=None): 
        self._x = x

    @property  #propriedade pega um metodo transforma numa (propriedade sintaxe atributo)
    def x(self):  #pega valor x e retorna, se não existir retorna 0
        return self._x or 0


    @x.setter # pega x cria uma modificação (setter) torna possivel alterar valor
    def x(self, value):  #pega valor x e retorna, se não existir retorna 0
        _x = self._x or 0   
        _value = value or 0
        self._x = _x + _value   # soma o valor


    @x.deleter # permite atribuir  (valor ex=0) sem tirar var da memória
    def x(self):
        self._x = -1  # põe -1 pra variável x


foo = Foo(10)
print( foo.x)
foo.x = 10
print( foo.x)
del foo.x
print( foo.x)                