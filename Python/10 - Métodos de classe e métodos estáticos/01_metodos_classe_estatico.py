"""métodos de classe e métodos estáticos
métodos de classe estão ligados a classe e não ao objeto, eles têm acesso ao estado 
da classe, pois recebem um parâmetro que aponta para classe e não para a instância do objeto  
por conveção chamado de cls  
"""


"""método estático não recebe um primeiro argumento explícito, ele também é um método vinculado à
classe e não ao objeto da classe, este método não pode acessar ou modificar o estado da classe, 
ele está presente em uma classe porque faz sentido que o método esteja presente na classe.  
"""


"""diferença entre eles
método classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método de 
estático não,
um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não,
pode acessá-lo ou modificá-lo."""

# métodos de classe usado quando retorna uma instancia 
#ex classe pessoa 

#métodos estáticos para criar funções utilitárias

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #transforma em método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod #decora sua função
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
