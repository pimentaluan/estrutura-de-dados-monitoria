class ContaBancaria:
    taxa_juros = 0.02  # atributo de classe

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

    @staticmethod
    def banco():
        return "Banco Python"

    @classmethod
    def alterar_juros(cls, nova_taxa):
        cls.taxa_juros = nova_taxa


# Demonstração
conta1 = ContaBancaria("Luan", 500)
conta1.exibir_saldo()
conta1.depositar(200)

print("Banco:", ContaBancaria.banco())
print("Taxa atual:", ContaBancaria.taxa_juros)
ContaBancaria.alterar_juros(0.03)
print("Nova taxa:", ContaBancaria.taxa_juros)
