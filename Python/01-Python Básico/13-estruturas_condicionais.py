# Estruturas condicionais
# A estrutura condicional permite o desvio de fluxo de controle,
#  quando determinadas expressões lógicas são atendidas.

# if == se----------------------------------------------------
import sys


saldo = 2000
saque = float(input("Informe o valor de saque: "))

if saldo >= saque:
    print("Realizamos saque!")

if saldo <= saque:
    print("Saldo insuficiente!")

# if / else   == se / senão------------------------------------

saldo = 2000
saque = float(input("Informe o valor de saque: "))

if saldo >= saque:
    print("Realizamos saque!")
else:
    print("Saldo insuficiente!")

# if / elif / else == se / senão se / senão---------------------
opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato:\n "))

if opcao ==1:
    valor = float(input("Informe a quantia para saque! "))

elif opcao ==2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opção inválida!")        