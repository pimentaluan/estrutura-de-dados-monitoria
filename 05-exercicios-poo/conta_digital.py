class ContaDigital:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Depósito inválido.")
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor

    def exibir(self):
        print(f"{self.titular} | Saldo: R${self.__saldo:.2f}")


# Teste
conta = ContaDigital("Luan", 1000)

try:
    conta.depositar(500)
    conta.sacar(200)
    conta.exibir()
    conta.sacar(2000)
except ValueError as erro:
    print(f"Erro: {erro}")
