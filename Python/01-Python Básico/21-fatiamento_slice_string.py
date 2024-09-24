# Fatiamento é usada para retornar substrings (parte da string original)
# Informando inicio start, fim stop e passo step: [start:stop[,step]]

nome = "Tifany de Camargo"
nome1 = "Tifany de Camargo"
nome3 = "Karol"

print(nome [0]) # informa primeiro caractere
# T

print(nome [:6]) # informa 6 primeiros caracteres
# Tifany

print(nome [10:]) # informa a partir 10° caractere
# Camargo

print(nome [7:9]) # informa a partir 7 ao 9 caractere
# de

print(nome1 [1:6:3]) # informa a partir 1 até 6 passo 3 
# in


print(nome1 [:]) # informa todos caractere
# Tifany de Camargo

print(nome3[::-1]) # Informe seu contrário de trás para frente
# loraK