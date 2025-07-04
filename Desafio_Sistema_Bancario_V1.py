menu = """

=========================================
             BANCO SAPHIRA
=========================================

Bem-vindo ao sistema bancário Saphira!
Por favor, escolha uma das opções abaixo:

[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Extrato
[ 0 ] Sair

=========================================

=>
"""

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > saldo:
        print("Saldo insuficiente para saque.")
    elif valor > limite:
        print(f"Saque não realizado. Valor do saque excede o limite de R$ {limite:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print(f"Saque não realizado. Número máximo de saques ({LIMITE_SAQUES}) atingido. Tente novamente amanhã.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato():
    global extrato
    if extrato:
        print("================ Extrato ================")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Nenhuma transação realizada.")

def main():
    global saldo, extrato, numero_saques
    while True:
        print(menu)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            sacar(valor)
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "0":
            print("Obrigado por usar o Banco Saphira! Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()