# Função são bloco de código, pode retornar valores.
#def indica que é função

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome): # obrigatório passar valor qdo chamar a função
    print(f"Seja bem vindo {nome}!")   

def exibir_mensagem3(nome="Anônimo"): # se torna opcional passar valor qdo chamar a função
    print(f"Seja bem vindo {nome}!") 

#chamando a função para executar
exibir_mensagem()
exibir_mensagem2(nome="Thiago") 
exibir_mensagem3() 
exibir_mensagem3(nome="Camargo")

