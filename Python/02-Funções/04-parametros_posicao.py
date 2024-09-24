# Positional Only

def criar_carro( Modelo, Ano, Placa, /,Marca, Motor, Combustivel ): #salva carro no banco de dados
    print( Modelo,Ano,Marca,Motor,Placa,Combustivel)

# Antes da barra tem que indicar por posição / apos barra posição ou nomeados tanto faz
criar_carro("Palio",1999, "ABC-1234",Marca="Fiat",Motor="1.0",Combustivel="Gasolina")