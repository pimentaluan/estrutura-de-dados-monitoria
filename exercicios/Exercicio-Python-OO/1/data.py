class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, valor):
        self.__dia = valor

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, valor):
        self.__mes = valor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"


if __name__ == "__main__":
    # Criando e testando o objeto
    data = Data(30, 4, 2025)
    print(f"Data completa: {data}")

    print(f"Dia: {data.dia}")
    print(f"Mês: {data.mes}")
    print(f"Ano: {data.ano}")

    data.dia = 11
    data.mes = 8
    data.ano = 2026
    print(f"Data completa: {data}")
