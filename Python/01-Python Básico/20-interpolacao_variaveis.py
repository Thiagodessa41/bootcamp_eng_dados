# Em python temos três formas de interpolar variáveis.
# Usando %, método format e f strings.
# A primeira forma não é atualmente recomendada seu uso em python três é rara.
# Por esse motivo iremos focar nas 2 últimas.

# -------------------------concatenar com old style %s %d %f-----------------------------
nome  = "Thiago"
idade = 42
profissao = "Analista de Dados"
linguagem = "Python"
# %s -> variável string
# %d -> variável number inteiro
# %f -> VARIÁVEL float ponto flutuante
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))
# Olá, me chamo Thiago. Eu tenho 42 anos de idade, trabalho como Analista de Dados e estou matriculado no curso de Python.

# -------------------------concatenar com .format {} -----------------------------
nome  = "Thiago"
idade = 42
profissao = "Cientista de Dados"
linguagem = "SQL"
# %s -> variável string
# %d -> variável number inteiro
# %f -> VARIÁVEL float ponto flutuante

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
# Olá, me chamo Thiago. Eu tenho 42 anos de idade, trabalho como Cientista de Dados e estou matriculado no curso de SQL.

# outra forma nesse caso descreva índice da  posição da variável sempre começa do 0 - 1- 2 - 3...
# Essa melhor forma
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format(linguagem,profissao,idade,nome))

# outra forma
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(linguagem=linguagem, profissao=profissao, idade=idade, nome=nome))

# outra forma usado dicionário---------------------------------------------------------------------
pessoa = {'nome': 'Thiago', 'idade': '42', 'profissao': 'Engenheiro de Dados', 'linguagem': 'Python'}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))
# Olá, me chamo Thiago. Eu tenho 42 anos de idade, trabalho como Engenheiro de Dados e estou matriculado no curso de Python.

# outra forma usado -> f antes do texto------------------------------------------------------------
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
# Olá, me chamo Thiago. Eu tenho 42 anos de idade, trabalho como Engenheiro de Dados e estou matriculado no curso de Python.


#-------------------------------------formatar strings com f-string--------------------------------
pi = 3.141516
print (f"Valor de PI: {pi:.2f}") # .2f -> exibe duas casas após vírgula.
#Valor de PI: 3.14"

print (f"Valor de PI: {pi:10.2f}") # (10 espaços) e (duas casas após a vírgula).
#Valor de PI:         3.14"