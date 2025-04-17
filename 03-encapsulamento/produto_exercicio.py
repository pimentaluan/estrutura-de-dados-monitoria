class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def exibir(self):
        print(f"Produto: {self.__nome} | Preço: R${self.__preco:.2f}")

    def aplicar_desconto(self, percentual):
        if percentual > 50:
            print("Desconto não permitido. Máximo: 50%.")
            return
        desconto = self.__preco * (percentual / 100)
        self.__preco -= desconto
        print(f"✔️ Desconto de {percentual}% aplicado. Novo preço: R${self.__preco:.2f}")

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            print("Preço inválido. Não pode ser negativo.")
        else:
            self.__preco = novo_preco


# Demonstração
produto = Produto("Fone de Ouvido", 200)
produto.exibir()
produto.aplicar_desconto(30)
produto.exibir()

produto.preco = -50  # Testando setter com validação
produto.preco = 150
produto.exibir()
