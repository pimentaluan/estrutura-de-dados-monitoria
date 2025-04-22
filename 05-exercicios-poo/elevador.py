class Elevador:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.pessoas = 0

    def entrar(self):
        if self.pessoas < self.capacidade:
            self.pessoas += 1
            print(f"Entrou uma pessoa. Total: {self.pessoas}")
        else:
            print("Elevador lotado!")

    def sair(self):
        if self.pessoas > 0:
            self.pessoas -= 1
            print(f"Uma pessoa saiu. Total: {self.pessoas}")
        else:
            print("Elevador vazio!")


# Teste
e = Elevador(3)
e.entrar()
e.entrar()
e.entrar()
e.entrar()
e.sair()
e.sair()
e.sair()
e.sair()
