class PilhaVazia(Exception):
    pass

class Node:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    @property
    def tamanho(self):
        return self._tamanho

    @property
    def vazia(self):
        return self._topo is None

    def empilhar(self, elemento):
        self._topo = Node(elemento, self._topo)
        self._tamanho += 1

    def desempilhar(self):
        if self.vazia:
            raise PilhaVazia()
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor

    def imprimir(self):
        atual = self._topo
        while atual:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()

    @property
    def topo(self):
        if self.vazia:
            raise PilhaVazia()
        return self._topo.valor


if __name__ == "__main__":
    p = PilhaEncadeada()
    p.empilhar(2)
    p.empilhar(15)
    p.empilhar(1)
    p.empilhar(10)
    p.empilhar(8)
    p.imprimir()
    print("Topo:", p.topo)
    print("Desempilhado:", p.desempilhar())
    p.imprimir()
