# break interrompe ciclo--------------------------------------------------------------------

while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10: # quando usuario digitir 10 para programa
        break

    print(numero)
  

for numero1 in range(100):

    if numero1 == 10: # para quando chegar 0 á 9
        break

    print(numero1, end=" ") #end= " " serve para exibir na mesma linha


    # Continue------------------------------------------------------------------------------
    #Não quero exibir o 12 

    for numero2 in range(20):

        if numero2 == 12: # ira desconsiderar o 12
            continue

    print(numero2, end=" ") #end= " " serve para exibir na mesma linha