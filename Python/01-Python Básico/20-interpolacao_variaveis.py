# Em python temos três formas de interpolar variáveis.
# Usando %, método format e f strings.
# A primeira forma não é atualmente recomendada seu uso em python três é rara.
# Por esse motivo iremos focar nas 2 últimas.

# -------------------------concatenar com old style %s %d %f-----------------------------
nome  = "Thiago"
idade = 42
profissao = "Programador"
linguagem = "Pyhton"
# %s -> variável string
# %d -> variável number inteiro
# %f -> VARIÁVEL float ponto flutuante
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))
# Olá, me chamo Thiago. Eu tenho 42 naos de idade, trabalho como Programador e utilizo e estou matriculado no curso de Python.

# -------------------------concatenar com .format {} -----------------------------
nome  = "Karol"
idade = 24
profissao = "Engenheira Dados"
linguagem = "Jungle"
# %s -> variável string
# %d -> variável number inteiro
# %f -> VARIÁVEL float ponto flutuante

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
# Olá, me chamo Karol. Eu tenho 24 naos de idade, trabalho como Engenheira Dados e utilizo e estou matriculado no curso de Jungle.


# outra forma nesse caso descreva índice da  posição da variável sempre começa do 0 - 1- 2 - 3...
# Essa melhor forma
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format(linguagem,profissao,idade,nome))
# Olá, me chamo Karol. Eu tenho 24 naos de idade, trabalho como Engenheira Dados e utilizo e estou matriculado no curso de Jungle.

# outra forma
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(linguagem=linguagem, profissao=profissao, idade=idade, nome=nome))
# Olá, me chamo Karol. Eu tenho 24 naos de idade, trabalho como Engenheira Dados e utilizo e estou matriculado no curso de Jungle.

# outra forma usado dicionário---------------------------------------------------------------------
pessoa = {'nome': 'Gustavo', 'idade': '13', 'profissao': 'estudante', 'linguagem': 'Robótica'}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))
# Olá, me chamo Gustavo. Eu tenho 13 naos de idade, trabalho como estudante e utilizo e estou matriculado no curso de Robótica.


# outra forma usado -> f antes do texto------------------------------------------------------------
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
# Olá, me chamo Karol. Eu tenho 24 naos de idade, trabalho como Engenheira Dados e utilizo e estou matriculado no curso de Jungle.


#-------------------------------------formatar strings com f-string--------------------------------
pi = 3.141516
print (f"Valor de PI: {pi:.2f}") # .2f -> exibe duas casas após vírgula.
#Valor de PI: 3.14"

print (f"Valor de PI: {pi:10.2f}") # (10 espaços) e (duas casas após a vírgula).
#Valor de PI:         3.14"