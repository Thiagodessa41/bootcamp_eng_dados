# escopo global
# variavel salario global esta fora da função

salario = 2000

def salario_bonus(bonus, lista):
    global salario #chamando variavel global
    lista.append(2) # append adiciona algo
    salario += bonus # somando com bonus
    return salario


lista = [1] # criou lista
novoSalario=salario_bonus(500, lista) 
print(novoSalario)
print(lista)
