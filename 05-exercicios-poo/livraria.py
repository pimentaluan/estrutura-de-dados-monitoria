class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.__preco = preco

    def exibir_info(self):
        print(f"{self.titulo} | Autor: {self.autor} | Preço: R${self.__preco:.2f}")

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            print("Preço inválido!")
        else:
            self.__preco = novo_preco


# Teste
livro = Livro("Python para Iniciantes", "João Silva", 49.90)
livro.exibir_info()
livro.preco = -10
livro.preco = 39.90
livro.exibir_info()
