class Conta_Corrente:
    def __init__(self, numero: int, saldo: float, nome_titular: str):
        self.__numero = numero
        self.__saldo = saldo
        self.__nome_titular = nome_titular

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nome_titular(self):
        return self.__nome_titular

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor: float):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def __str__(self):
        return f"Conta: {self.numero} | Titular: {self.nome_titular} | Saldo: R$ {self.saldo:.2f}"
