def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Fim da operação.")


# Testes
dividir(10, 2)
dividir(5, 0)
