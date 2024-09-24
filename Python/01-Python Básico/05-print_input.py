nome = input('Informe seu nome! ')
print(nome)

#end serve para adicionar algo no final da frase
idade = input('Informe sua idade! ')
print(nome, idade, end="... \n")

nome1 = input('Informe outro nome! ')
print(nome1)

#sep serve para colocar separador
idade1 = input('Informe outra idade! ')
print(nome1, idade1, sep="#")
print(nome1, idade1, sep="#", end="... \n")

print(f'Meu nome é {nome1} tenho {idade1} anos de idade.')
