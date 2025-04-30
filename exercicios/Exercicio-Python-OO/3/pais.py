class Pais:
    def __init__(self, nome:str, capital:str, dimensao:int):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteiras = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def capital(self):
        return self.__capital
    
    @property
    def dimensao(self):
        return self.__dimensao
    
    @property
    def fronteiras(self):
        return self.__fronteiras
    
    def add_fronteira(self, pais):
        if pais not in self.__fronteiras:
            self.__fronteiras.append(pais)

    def __str__(self):
        return f"Nome: {self.nome}\nCapital: {self.capital}\nDimensão: {self.dimensao} Km²\nFronteiras: {self.fronteiras}"
        

if __name__ == "__main__":
    pais = Pais("Brasil", "Brasília", 8515767)
    pais.add_fronteira("Argentina")
    pais.add_fronteira("Uruguai")
    pais.add_fronteira("Paraguai")
    pais.add_fronteira("Argentina")
    print(pais)