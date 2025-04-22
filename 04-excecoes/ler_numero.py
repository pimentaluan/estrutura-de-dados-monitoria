def ler_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"Você digitou: {numero}")
            break
        except ValueError:
            print("❌ Valor inválido. Por favor, digite um número inteiro.")


# Teste
ler_numero()
