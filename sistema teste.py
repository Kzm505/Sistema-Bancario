menu = ("""
      ############ Menu ############
      
      1 - Depositar
      2 - Sacar
      3 - Extrato
      0 - Cancelar
      """)

saldo = 0
limite = 500  # reais
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3  # saques diários

while True:
    opcao = input(menu).strip()  # Pegando a opção do usuário e removendo espaços extras

    if opcao == "1":
        valor = float(input("Insira a quantia que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor:.2f}\n"
        else:
            print("O valor informado é inválido, a operação falhou")

    elif opcao == "2":
        valor = float(input("Insira a quantia que deseja sacar: "))

        passou_do_saldo = valor > saldo
        passou_do_limite = valor > limite
        passou_do_limite_diario = numero_saques >= LIMITE_SAQUES

        if passou_do_saldo:
            print("Operação cancelada, saldo insuficiente")
        elif passou_do_limite:
            print("Operação cancelada, limite ultrapassado")
        elif passou_do_limite_diario:
            print("Operação cancelada, limite diário de saques atingido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1
        else:
            print("O valor informado é inválido, a operação falhou")

    elif opcao == "3":
        print("############# Extrato #############")
        print("\nNão houve nenhuma movimentação na conta" if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("###################################")

    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor, selecione uma opção válida.")
