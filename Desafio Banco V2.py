import textwrap

menu = """
########## Banco ##########
    
1 - Deposito
2 - Sacar
3 - Extrato
4 - Criar usuário
5 - Criar conta
6 - Listar contas
7 - Sair
    
Digite a operação desejada: """


def deposito(saldo, extrato_conta, /):

    print("########## Deposito ##########\n")

    valor = float(input("\nDigite o valor para deposito: "))

    if valor > 0:

        saldo += valor
        extrato_conta += f"Deposito no valor de R${valor:.2f}\n"

        print(f"Deposito no valor de R${valor:.2f} efetuado!")

    else:

        print("Valor para deposito invalido!")

    return saldo, extrato_conta


def saque(*, saldo, saque_maximo, extrato_conta, numero_saque, limite_saque):

    valor = float(input("Digite o valor que deseja sacar: "))

    if numero_saque >= limite_saque:
        print("Limite de saque diario atingido!")
    elif valor > saque_maximo:
        print("O limite de saque é de R$500,00")
    elif valor > saldo:
        print("O saldo é insuficiente para realizar o saque!")
    else:
        saldo -= valor
        extrato_conta += f"Saque no valor de R${valor:.2f}\n"
        numero_saque += 1
        print(f"Saque no valor de R${valor:.2f} realizado!")

    return saldo, extrato_conta, numero_saque


def extrato(saldo, extrato_conta):

    print("########## Extrato da conta ##########\n")
    print(f"Seu saldo atual é R${saldo:.2f}\n")
    print("----- Movimentações feitas na conta -----\n")
    print("Não foram feitas movimentações na conta!" if not extrato_conta else extrato_conta)


def criar_usuario(usuarios):

    print("########## Cadastrar usuário ##########\n")
    cpf = input("Digite seu cpf: ")
    usuario = listar_usuarios(usuarios, cpf)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print("Usuário criado com sucesso!")


def listar_usuarios(usuarios, cpf):

    usuarios_listados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_listados[0] if usuarios_listados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = listar_usuarios(usuarios, cpf)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    saldo = 0
    saque_maximo = 500
    extrato_conta = ''
    numero_saque = 0
    limite_saque = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = input(menu)

        if opcao == '1':
            saldo, extrato_conta = deposito(saldo, extrato_conta)
        elif opcao == '2':
            saldo, extrato_conta, numero_saque = saque(
                saldo=saldo, saque_maximo=saque_maximo, extrato_conta=extrato_conta,
                numero_saque=numero_saque, limite_saque=limite_saque
            )
        elif opcao == '3':
            extrato(saldo, extrato_conta)
        elif opcao == '4':
            criar_usuario(usuarios)
        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            break
        else:
            print('Operação invalida. Selecione uma operação valida!')


main()
