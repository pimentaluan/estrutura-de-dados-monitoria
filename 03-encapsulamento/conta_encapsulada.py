class Conta:
    def __init__(self, titular, saldo):
        self.__titular = titular     # atributo privado
        self.__saldo = saldo         # atributo privado

    def exibir_saldo(self):
        print(f"{self.__titular}, seu saldo é R${self.__saldo:.2f}")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido para depósito.")


# Demonstração
conta = Conta("Luan", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()

# Tentando acessar diretamente (vai falhar)
try:
    print(conta.__saldo)
except AttributeError:
    print("Acesso direto negado: atributo privado.")
