class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir(self):
        print(f"{self.nome} - {self.telefone}")


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

    def listar(self):
        if not self.contatos:
            print("Agenda vazia.")
        else:
            for c in self.contatos:
                c.exibir()

    def buscar(self, nome):
        for c in self.contatos:
            if c.nome.lower() == nome.lower():
                return c
        raise LookupError("Contato não encontrado.")


# Teste
agenda = Agenda()
agenda.adicionar(Contato("Luan", "(83)99999-9999"))
agenda.adicionar(Contato("Ana", "(83)98888-8888"))

agenda.listar()

try:
    resultado = agenda.buscar("João")
    resultado.exibir()
except LookupError as erro:
    print(f"Erro: {erro}")
