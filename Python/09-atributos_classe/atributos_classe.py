"""atributos do objeto
    todos objetos nascem com mesmo número de atributos de classe e de instância
    atributos de instância são diferentes para cada objeto objeto tem uma cópia, já
    os atributos de classe são compartilhados entre os objetos.
"""

class Estudante:
    escola = "DIO" # toda (variavel de classe) declarada logo apos def da classe

    # construtor
    def __init__(self, nome, matricula):
        self.nome = nome              #lembra que o (self) é instância
        self.matricula = matricula

    # formato de impressão
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1) # duas variáveis que armz as instancia de (estudante)
aluno_2 = Estudante("Giovanna", 2) # duas variáveis que armz as instancia de (estudante)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" #trocou nome da escola
aluno_3 = Estudante("Chappie", 3) # todos objetos (alunos), pertence a nova escola
mostrar_valores(aluno_1, aluno_2, aluno_3)