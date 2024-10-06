import textwrap  # Importa a biblioteca textwrap para formatação de texto

def menu():
    # Define o menu de opções
    menu = """
    ======================== MENU ========================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair

    => """
    return input(textwrap.dedent(menu))  # Retorna a opção escolhida pelo usuário

def depositar(saldo, valor, extrato):
    if valor > 0:  # Verifica se o valor é positivo
        saldo += valor  # Atualiza o saldo com o valor do depósito
        extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona o depósito ao extrato
        print("Depósito realizado com sucesso.")
    else:  # Caso o valor seja inválido (negativo ou zero)
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato  # Retorna o saldo e extrato atualizados

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo  # Verifica se o saque excede o saldo
    excedeu_limite = valor > limite  # Verifica se o saque excede o limite
    excedeu_saques = numero_saques >= limite_saques  # Verifica se o número máximo de saques foi excedido

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedidos.")
    elif valor > 0:  # Verifica se o valor do saque é positivo
        saldo -= valor  # Atualiza o saldo subtraindo o valor do saque
        extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona o saque ao extrato
        numero_saques += 1  # Incrementa o contador de saques
        print("Saque realizado com sucesso.")
    else:  # Se o valor for inválido
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques  # Retorna o saldo e extrato atualizados

def extrato_func(saldo, extrato):
    print("\n============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)  # Exibe o extrato ou mensagem de vazio
    print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
    print("=====================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")  # Solicita o CPF do usuário
    usuario = filtrar_usuarios(cpf, usuarios)  # Verifica se já existe um usuário com o CPF informado

    if usuario:  # Se o usuário já existir
        print("Já existe usuário com esse CPF")
        return  # Encerra a função

    # Coleta os dados do novo usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  # Adiciona o usuário à lista

    print("Usuário criado com sucesso")  # Mensagem de confirmação

def filtrar_usuarios(cpf, usuarios):
    # Filtra a lista de usuários com base no CPF
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None  # Retorna o usuário encontrado ou None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")  # Solicita o CPF do usuário
    usuario = filtrar_usuarios(cpf, usuarios)  # Verifica se o usuário existe

    if usuario:  # Se o usuário foi encontrado
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}  # Retorna os dados da conta criada

    print("Usuário não encontrado, fluxo de criação de conta encerrado")  # Mensagem de erro

def listar_contas(contas):
  for conta in contas:
    linha = f"""\
      Agência:{conta['agencia']}
      C/C: {conta['numero_conta']}
      Titular: {conta['usuario']['nome']}
    """
    print("-" *100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3  # Limite máximo de saques
    AGENCIA = "0001"  # Código da agência
    saldo = 0  # Inicializa o saldo
    limite = 500  # Define o limite de saque
    extrato = ""  # Inicializa o extrato
    numero_saques = 0  # Inicializa o contador de saques
    usuarios = []  # Lista de usuários
    contas = []  # Lista de contas

    while True:  # Loop principal do programa
        opcao = menu()  # Mostra o menu e obtém a opção escolhida

        if opcao == "d":  # Depósito
            valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
            saldo, extrato = depositar(saldo, valor, extrato)  # Chama a função de depósito

        elif opcao == "s":  # Saque
            valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            ) # Chama a função de saque

        elif opcao == "e":  # Extrato
            extrato_func(saldo, extrato)  # Chama a função de extrato

        elif opcao == "q":  # Sair
            break  # Encerra o loop e o programa

        elif opcao == "nu":  # Novo Usuário
            criar_usuario(usuarios)  # Chama a função para criar um novo usuário

        elif opcao == "nc":  # Nova Conta
            numero_conta = len(contas) + 1  # Define o número da nova conta
            conta = criar_conta(AGENCIA, numero_conta, usuarios)  # Chama a função para criar uma nova conta

            if conta:  # Se a conta foi criada com sucesso
                contas.append(conta)  # Adiciona a conta à lista de contas
                
        elif opcao == "lc": # Listar Contas
            listar_contas(contas)
          
        else:  # Se a opção for inválida
            print("Operação inválida, por favor selecione novamente a operação desejada")  # Mensagem de erro


# Inicia o programa chamando a função main
main()
