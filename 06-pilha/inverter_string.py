from pilha_encadeada import PilhaEncadeada

def inverter_string(texto):
    pilha = PilhaEncadeada()
    for caractere in texto:
        pilha.empilhar(caractere)

    resultado = ""
    while not pilha.vazia:
        resultado += pilha.desempilhar()
    return resultado


if __name__ == "__main__":
    entrada = "PYTHON"
    print("Original:", entrada)
    print("Invertida:", inverter_string(entrada))
