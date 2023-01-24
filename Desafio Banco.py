import locale

saldo = 0
saque_diario = 3
limite_saque = 500
extrato_bancario = []

locale.setlocale(locale.LC_ALL, 'pt-br.UTF-8')

def main():

    print("########## Bem-vindo ao sistema de banco ########## \n")
    print("Neste sistema do banco, você pode realizar operações como: \n")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Consultar extrato \n")

    operacao = int(input("Digite a operação desejada: "))

    if operacao == 1:
        saque()
    elif operacao == 2:
        deposito()
    elif operacao == 3:
        extrato()


def saque():

    global saldo
    global saque_diario

    print("\n ########## Operação de saque ########## \n")

    if saque_diario == 0:
        print('Limite de saque diario atingido! Você poderá realizar mais saques amanhã!')
        main()
    else:

        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if valor_saque > saldo:
            print("\nO saldo é insuficiente para realizar a operação!\n")
        elif valor_saque > 500:
            print("\nO limite máximo para saque é de R$500,00 por saque! \n")
        elif valor_saque < 10:
            print("\nO valor minimo para saque é R$10,00")
        else:
            print(f"Saque realizado com sucesso! Você sacou R${locale.currency(valor_saque)}\n")

            saque_diario -=1

            saldo -= valor_saque

            extrato_bancario.append(f"Saque no valor de {locale.currency(valor_saque)} realizado!")


    print("Deseja realizar outro saque? \n")
    print("1 - Sim")
    print("2 - Não e voltar ao menu")
    print("3 - Não e sair")

    acao = int(input("\n Digite a operação desejada: "))

    if acao == 1:
        saque()
    elif acao == 2:
        main()
    elif acao == 3:
        quit()
    else:
        print("Opção invalida! Programa encerrado.")

def deposito():

    global saldo

    print("\n ########## Operação de deposito ########## \n")

    valor_deposito = float(input("Digite o valor que deseja depositar: "))

    if str(valor_deposito).startswith("-"):

        print("Só é possivel depositar um valor positivo na conta!")

        deposito()

    else:

        print(f"\nDeposito realizado com sucesso! Você depositou R${locale.currency(valor_deposito)} \n")

        saldo = saldo + valor_deposito

        extrato_bancario.append(f"Deposito no valor de {locale.currency(valor_deposito)} realizado!")

        print("Deseja realizar outro deposito? \n")
        print("1 - Sim")
        print("2 - Não e voltar ao menu")
        print("3 - Não e sair")

        acao = int(input("\n Digite a operação desejada: "))

        if acao == 1:
            deposito()
        elif acao == 2:
            main()
        elif acao == 3:
            quit()
        else:
            print("Opção invalida! Programa encerrado.")


def extrato():

    print("\n ########## Operação de extrato ########## \n")

    print(f"Seu saldo é {saldo} \n")

    print("Operações realizadas na conta:\n")

    for acoes in extrato_bancario:
        print(acoes)

    print("Deseja ver o extrato da sua conta novamente? \n")
    print("1 - Sim")
    print("2 - Não e voltar ao menu")
    print("3 - Não e sair")

    acao = int(input("\n Digite a operação desejada: "))

    if acao == 1:
        extrato()
    elif acao == 2:
        main()
    elif acao == 3:
        quit()
    else:
        print("Opção invalida! Programa encerrado.")

        
main()