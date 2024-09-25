# python não tem qword pra fazer encapsulamento são convenções

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property #ira permitir acessar o valor dentro da variavel
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Thiago", 1982)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
