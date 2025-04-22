class PilhaSimples:
    def __init__(self):
        self._dados = []

    def empilhar(self, elemento):
        self._dados.append(elemento)

    def desempilhar(self):
        return self._dados.pop()

    def imprimir(self):
        for elemento in self._dados:
            print(elemento, end=" ")
        print()

    @property
    def topo(self):
        return self._dados[-1]


if __name__ == "__main__":
    p = PilhaSimples()
    p.empilhar("A")
    p.empilhar("B")
    p.empilhar("C")
    p.imprimir()
    print("Topo:", p.topo)
    print("Desempilhado:", p.desempilhar())
    p.imprimir()
