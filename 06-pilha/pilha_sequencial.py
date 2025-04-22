from array import Array

class PilhaVazia(Exception):
    pass

class PilhaSequencial:
    def __init__(self):
        self._dados = Array(tamanho=3)
        self._topo = 0

    @property
    def tamanho(self):
        return self._topo

    @property
    def vazia(self):
        return self.tamanho == 0

    @property
    def cheia(self):
        return self.tamanho == self._dados.tamanho

    def _redimensionar(self):
        antigos = self._dados
        novos = Array(antigos.tamanho * 2)
        novos.copiar_de(antigos)
        self._dados = novos

    def empilhar(self, elemento):
        if self.cheia:
            self._redimensionar()
        self._dados.set(self._topo, elemento)
        self._topo += 1

    def desempilhar(self):
        if self.vazia:
            raise PilhaVazia()
        self._topo -= 1
        elemento = self._dados.get(self._topo)
        self._dados.set(self._topo, None)
        return elemento

    def imprimir(self):
        for i in range(self._topo):
            print(self._dados.get(i), end=" ")
        print()

    @property
    def topo(self):
        if self.vazia:
            raise PilhaVazia()
        return self._dados.get(self._topo - 1)


if __name__ == "__main__":
    p = PilhaSequencial()
    p.empilhar(10)
    p.empilhar(20)
    p.empilhar(30)
    p.empilhar(40)  # força redimensionamento
    p.imprimir()
    print("Topo:", p.topo)
    print("Desempilhado:", p.desempilhar())
    p.imprimir()
