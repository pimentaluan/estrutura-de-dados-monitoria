class Carro:
    limite_velocidade = 180  # atributo de classe

    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = 0

    def acelerar(self, valor):
        nova_velocidade = self.velocidade_atual + valor
        if nova_velocidade > Carro.limite_velocidade:
            self.velocidade_atual = Carro.limite_velocidade
        else:
            self.velocidade_atual = nova_velocidade

    def frear(self, valor):
        nova_velocidade = self.velocidade_atual - valor
        if nova_velocidade < 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual = nova_velocidade

    def exibir_velocidade(self):
        print(f"Carro: {self.modelo} | Ano: {self.ano}")
        print(f"Velocidade atual: {self.velocidade_atual} km/h")


# Demonstração
carro1 = Carro("Uno", 2015)
carro1.acelerar(50)
carro1.frear(10)
carro1.exibir_velocidade()
