from conta_corrente import Conta_Corrente
def encontrar_conta(contas, numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None

if __name__ == "__main__":
    contas = []

    print("Cadastro de 10 contas bancárias:")
    for i in range(10):
        print(f"\nCadastro da conta {i+1}")
        numero = int(input("Número da conta: "))
        nome = input("Nome do titular: ")
        saldo_inicial = float(input("Saldo inicial: "))
        conta = Conta_Corrente(numero, saldo_inicial, nome)
        contas.append(conta)

    while True:
        print("\n--- MENU ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar saldo")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = int(input("Número da conta para depósito: "))
            conta = encontrar_conta(contas, numero)
            if conta:
                valor = float(input("Valor a depositar: "))
                conta.depositar(valor)
                print("Depósito realizado.")
            else:
                print("Conta não encontrada.")

        elif opcao == "2":
            numero = int(input("Número da conta para saque: "))
            conta = encontrar_conta(contas, numero)
            if conta:
                valor = float(input("Valor a sacar: "))
                if conta.sacar(valor):
                    print("Saque realizado com sucesso.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            numero = int(input("Número da conta para consulta: "))
            conta = encontrar_conta(contas, numero)
            if conta:
                print(conta)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
