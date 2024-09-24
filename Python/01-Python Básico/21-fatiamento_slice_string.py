# Fatiamento é usada para retornar substrings (parte da string original)
# Informando inicio start, fim stop e passo step: [start:stop[,step]]

nome = "Thiago Camargo"
nome1 = "Fulano de Tal"
nome3 = "Ciclano"

print(nome[0]) # informa primeiro caractere
# T

print(nome[:6]) # informa 6 primeiros caracteres
# Thiago

print(nome[10:]) # informa a partir 10° caractere
# margo

print(nome1[7:9]) # informa a partir 7 ao 9 caractere
# de

print(nome1[1:6:3]) # informa a partir 1 até 6 passo 3 
# in

print(nome1 [:]) # informa todos caractere
# Fulano de Tal

print(nome3[::-1]) # Informe seu contrário de trás para frente
# onalciC