class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_info(self):
        print(f"Livro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")

    def atrasado(self):
        if self.ano < 2000:
            return "Antigo"
        else:
            return "Atual"


# Criando objeto
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)

# Exibindo informações
livro1.exibir_info()
print("Classificação:", livro1.atrasado())
