conta_normal = True
conta_universitaria = False

saldo = 2000
cheque_especial = 450
saque = int(input("Informe o valor de saque! "))

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso, com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")    

# Agora exemplo com conta universitária
conta_normal = False
conta_universitaria = True

saldo = 2000
cheque_especial = 450
saque = int(input("Informe o valor de saque! "))

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso, com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")  