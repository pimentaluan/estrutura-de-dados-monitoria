def sacar(valor, saldo):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor


# Testando com tratamento
saldo_atual = 1000

try:
    novo_saldo = sacar(1500, saldo_atual)
    print(f"Saque realizado com sucesso! Novo saldo: R${novo_saldo:.2f}")
except ValueError as erro:
    print(f"❌ Erro ao sacar: {erro}")
