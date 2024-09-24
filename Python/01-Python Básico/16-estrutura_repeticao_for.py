# for e while são utilida para repetir um trecho de código determinado numero de vezes.
# for usa quando sabemos o numero exato de vezes

texto = input("Informe um texto: ")
vogais = "AEIOU"

# iteravel
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print()  # adiciona quebra de linha


texto =()
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()  # adiciona quebra de linha
    print("Executado no final do laço")    


#Função range usa para produzir uma sequencia de números inteiros a partir de um inicio
# range (stop) -> range object
# range (start, stop[, step]) -> range object

#Range
# Exibindo a tabuada 5
for numero in range(0,51,5): #start=0 , stop=51 , step=5
    print(numero, end=" ")




