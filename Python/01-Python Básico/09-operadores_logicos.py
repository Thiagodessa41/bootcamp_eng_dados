# op_comparacao + op_logico + op_comparacao ...N...

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite # AND tudo tem que ser true

saldo >= saque or saque <= limite # OR apenas um tem que ser true


# Operador de negação
contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500;"


not ""

# Cenário de sistema bancário

saldo1 = 1000
saque1 = 250
limite1 = 200
conta_especial1 = True

exp= saldo1 >= saque1 and saque1 <= limite1 or conta_especial1 and saldo1 >= saque1
print(exp)

exp1 = (saldo1 >= saque1 and saque1 <= limite1) or (conta_especial1 and saldo1 >= saque1)
print(exp1)