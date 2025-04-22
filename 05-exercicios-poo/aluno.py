class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        m = self.media()
        if m >= 7:
            return "Aprovado"
        elif m >= 5:
            return "Recuperação"
        else:
            return "Reprovado"


# Teste
aluno = Aluno("Maria", 6.0, 7.0)
print(f"{aluno.nome} - Média: {aluno.media():.1f} - Situação: {aluno.situacao()}")
