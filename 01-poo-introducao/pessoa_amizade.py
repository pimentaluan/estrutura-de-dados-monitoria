class Pessoa:
    def __init__(self, nome, idade, amigo=None):
        self.nome = nome
        self.idade = idade
        self.amigo = amigo

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")

    def ver_amizade(self):
        if self.amigo:
            print(f"{self.nome} é amigo de {self.amigo.nome}.")
        else:
            print(f"{self.nome} ainda não tem amigo cadastrado.")

    def set_amigo(self, amigo):
        self.amigo = amigo


# Criando objetos
p1 = Pessoa("Luan", 20)
p2 = Pessoa("Maria", 20)

p1.apresentar()
p2.apresentar()

# Definindo amizade e exibindo
p1.set_amigo(p2)
p1.ver_amizade()
