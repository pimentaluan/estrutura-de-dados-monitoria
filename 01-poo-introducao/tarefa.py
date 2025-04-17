class Tarefa:
    def __init__(self, titulo, feita, entrega, pessoa):
        self.titulo = titulo
        self.feita = feita
        self.entrega = entrega
        self.pessoa = pessoa

    def exibir(self):
        status = "✔️ Feita" if self.feita else "❌ Pendente"
        print(f"Tarefa: {self.titulo} | Entrega: {self.entrega} | Responsável: {self.pessoa} | Status: {status}")


# Criando objetos
tarefa1 = Tarefa("Lavar a louça", True, "2025-04-20", "Luan")
tarefa2 = Tarefa("Estudar para prova", False, "2025-04-22", "Ana")

# Exibindo informações
tarefa1.exibir()
tarefa2.exibir()
