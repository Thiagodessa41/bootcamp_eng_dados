# Argumentos nomeados
#Passa chave e valor

def salvar_carro(Marca, Modelo, Ano, Placa): #salva carro no banco de dados
    print(f"Carro inserido com sucesso! {Marca}/{Modelo}/{Ano}/{Placa}")


# Existe três formas de passar valor
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(Marca="Fiat", Modelo="Palio", Ano=1999, Placa="ABC-1234")
salvar_carro(**{"Marca":"Fiat", "Modelo": "Palio", "Ano": 1999, "Placa": "ABC-1234"})


#Podemos passar parâmetros obrigatórios com args e kwargs
# *args = passa como uma Tupla passa valores separados por vírgula dentro parenteses
# **kwargs passa como dicionário

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n\{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Sexta-feira, 26 Agosto de 2022",
    "Zen of Python",
    "Beautiful is better then ugly.",
    "Explicity is better than implicit.", 
    "Simple is better than complex",    
    autor="Tim Peters", ano=1999)    