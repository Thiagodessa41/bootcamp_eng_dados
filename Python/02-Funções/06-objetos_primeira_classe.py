
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def test(a,b):
    return a *  2 + b * 3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print (f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar) # 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # 10 - 10 = 0
exibir_resultado(10, 10, test) # 10 - 10 = 50
