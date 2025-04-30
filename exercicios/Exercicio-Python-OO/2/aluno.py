class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return str(self.__matricula)

    def media(self):
        if not self.__notas:
            return 0
        # Forma tradicional, melhor aprender assim para o resto da disciplina ficar mais fácil:
        soma = 0
        for nota in self.__notas:
            soma += nota
        return soma / len(self.__notas)
    
        # Forma compacta com função nativa do Python, assim não precisaria criar a variável soma e fazer o for para somar:
        # return sum(self.__notas) / len(self.__notas)

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def adiciona_nota(self, nota):
        self.__notas.append(nota)

if __name__ == "__main__":
    aluno = Aluno(20231370042, "Luan", [100, 90, 80])
    print(f"Matrícula: {aluno.matricula}")
    print(f"Nome: {aluno.nome}")

    print("Média:", aluno.media())

    aluno.nome = "Davi"
    print(f"Nome: {aluno.nome}")

    aluno.adiciona_nota(100)
    print("Nova média:", aluno.media())
